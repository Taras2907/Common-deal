<template>
  <div
    class="tab-pane fade"
    id="registration"
    role="tabpanel"
    aria-labelledby="pills-profile-tab"
  >
    <div class="container">
      <form @submit.prevent="registerUser">
        <div class="row">
          <div class="col-12">
            <div class="form-group">
              <label for="registerName">Username</label>
              <input
                @blur="validateUsername(username)"
                v-model="username"
                name="username"
                type="text"
                class="form-control"
                id="registerName"
                aria-describedby="loginHelp"
                placeholder="Enter name"
                required
              />

              <div v-if="usernameErrors">
                <p class="text-left mt-2">
                  <small
                    class="text-danger row ml-1"
                    v-for="(message, index) in usernameErrors"
                    :key="index"
                    >{{ message }}
                  </small>
                </p>
              </div>
              <small v-else id="registerHelp" class="form-text text-muted"
                >Fill the form and press submit to create account
              </small>
            </div>

            <div class="form-group">
              <label for="registerPassword">Password</label>
              <input
                @blur="validatePassword(password1)"
                v-model="password1"
                name="password1"
                type="password"
                class="form-control"
                id="registerPassword"
                placeholder="Password"
                autocomplete="off"
                required
              />
              <p class="text-left mt-2">
                <small
                  class="text-danger row ml-1"
                  v-for="(message, index) in passwordErrors"
                  :key="index"
                  >{{ message }}
                </small>
              </p>
            </div>

            <div class="form-group">
              <label for="passwordConfirmation">Confirm Password</label>
              <input
                @blur="checkPasswords"
                v-model="password2"
                name="password2"
                type="password"
                class="form-control"
                id="passwordConfirmation"
                placeholder="Confirm Password"
                autocomplete="off"
                required
              />
              <p v-if="confirmPasswordError" class="text-left mt-2">
                <small class="text-danger row ml-1"
                  >Password and confirm password does not match
                </small>
              </p>
            </div>

            <div class="form-group">
              <label for="registerEmail">Email</label>
              <input
                @blur="checkEmailExists(email)"
                v-model="email"
                name="email"
                type="email"
                class="form-control"
                id="registerEmail"
                placeholder="Email"
                required
                pattern="[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
              />
              <p class="text-left mt-2">
                <small
                  class="text-danger row ml-1"
                  v-for="(message, index) in emailErrors"
                  :key="index"
                  >{{ message }}
                </small>
              </p>
            </div>

            <button
              v-if="isRegistering"
              class="btn btn-primary"
              type="button"
              disabled
            >
              <span
                class="spinner-grow spinner-grow-sm"
                role="status"
                aria-hidden="true"
              ></span>
              Loading...
            </button>
            <button
              v-else
              :disabled="thereAreErrors || fieldsAreEmpty"
              type="submit"
              class="btn btn-primary"
              id="registerSubmit"
            >
              Submit
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
  import {apiService} from "../common/apiService";

  export default {
    name: "RegistrationComponent",
    data() {
      return {
        username: "",
        password1: "",
        password2: "",
        email: null,
        isRegistering: false,
        usernameErrors: null,
        passwordErrors: null,
        confirmPasswordError: false,
        emailErrors: null,
      }
    },
    computed: {
      thereAreErrors() {
        return (this.usernameErrors !== null &&
            this.passwordErrors !== null &&
            this.emailErrors !== null &&
            this.confirmPasswordError !== false);
      },
      fieldsAreEmpty() {
        return this.username === null || this.username === "" ||
            this.password1 === null || this.password1 === "" ||
            this.password2 === null || this.password2 === "" ||
            this.email === null || this.email === "";
      },
    },
    methods: {
      registerUser() {
        let endpoint = `/api/rest-auth/registration/`;
        let data = {
          username: this.username,
          password1: this.password1,
          password2: this.password2,
          email: this.email
        };
        this.isRegistering = true;
        apiService(endpoint, 'POST', data)
            .then(response => response.json())
            .then(responseData => {
              this.isRegistering = false;
              if (!responseData.key) {
                this.applyErrors(responseData)
              }else{
                this.username = '';
                this.password1 = '';
                this.password2 = '';
                this.email = '';
                this.$emit('switch-tab');
                location.reload();
              }
            })
            .catch(error => console.log(error))
      },
      applyErrors(responseData) {
        if (responseData.username) {
          this.usernameErrors = responseData.username
        }
        if (responseData.email) {
          this.emailErrors = responseData.email
        }
        if (responseData.password1) {
          this.passwordErrors = responseData.password1
        }
      },
      checkPasswords() {
        this.confirmPasswordError =
            ((this.password1 !== this.password2)
                && this.password1 !== "" && (this.password2 !== "" && this.password2 !== null));
      },
      checkUserNameExists(username) {
        let endpoint = '/api/rest-auth/user/name/';
        apiService(endpoint, "POST", {username: username})
            .then(response => response.json())
            .then(json_response => {
              if (json_response.message) {
                this.usernameErrors = [json_response.message]
              } else {
                this.usernameErrors = null;
              }
            })
            .catch(error => console.log(error))

      },
      checkEmailExists(email) {
        let endpoint = '/api/rest-auth/user/email/';
        apiService(endpoint, "POST", {email: email})
            .then(response => response.json())
            .then(json_response => {
              if (json_response.response.exists) {
                this.emailErrors = [json_response.response.message]
              } else {
                this.emailErrors = null
              }
            })
            .catch(error => console.log(error))
      },
      validateUsername(username) {
        if ((username.length < 4 || username.length > 15) && username !== "") {
          this.usernameErrors = ["Username should be between 5 and 15 symbols "]
        } else {
          this.usernameErrors = null;
          this.checkUserNameExists(username)
        }
      },
      validatePassword(password) {
        this.checkPasswords();
        if ((password.length < 7 || password.length > 15) && password !== "") {
          this.passwordErrors = ["Password should be between 8 and 15 symbols"]
        } else {
          this.passwordErrors = null;
          if (!isNaN(password) && password !== "") {
            this.passwordErrors = ["Password should not be entirely numeric"];
          } else {
            this.passwordErrors = null;
          }
        }
      }
    }
  }
</script>

<style scoped>

</style>