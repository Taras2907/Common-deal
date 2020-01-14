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
                    >{{ message }}</small
                  >
                </p>
              </div>
              <small v-else id="registerHelp" class="form-text text-muted"
                >Enter your login and password and press submit button
              </small>
            </div>

            <div class="form-group">
              <label for="registerPassword">Password</label>
              <input
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
                  >{{ message }}</small
                >
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
                  >Password and confirm password does not match</small
                >
              </p>
            </div>

            <div class="form-group">
              <label for="registerEmail">Email</label>
              <input
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
                  >{{ message }}</small
                >
              </p>
            </div>

            <button type="submit" class="btn btn-primary" id="registerSubmit">
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
        username: null,
        password1: null,
        password2: null,
        email: null,
        isRegistering: false,
        usernameErrors: null,
        passwordErrors: null,
        confirmPasswordError: false,
        emailErrors: null,
      }
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
        apiService(endpoint, 'POST', data)
            .then(response => response.json())
            .then(responseData => {
              if (!responseData.key) {
                this.applyErrors(responseData)
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
        this.confirmPasswordError = this.password1 !== this.password2;
      }
    }
  }
</script>

<style scoped>

</style>