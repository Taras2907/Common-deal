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
                pattern="^[a-zA-Z0-9]([._](?![._])|[a-zA-Z0-9]){6,18}[a-zA-Z0-9]$"
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
                  >{{ message }}</small
                >
              </p>
            </div>

            <button
                    :disabled="thereAreErrors || fieldsAreEmpty"
                    type="submit"
                    class="btn btn-primary"
                    id="registerSubmit">
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
    computed:{
      thereAreErrors(){
        return !(this.usernameErrors === null &&
                this.passwordErrors === null &&
                this.emailErrors === null &&
                this.confirmPasswordError === false);
      },
      fieldsAreEmpty(){
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
      },
      checkUserNameExists(username){
        let endpoint = '/api/rest-auth/user/name/';
        apiService(endpoint, "POST", {username: username})
                .then(response => response.json())
                .then(json_response => {
                    if(json_response.message){
                      this.usernameErrors = [json_response.message]
                    }else{
                      this.usernameErrors = null;
                    }
                })
                .catch(error => console.log(error))

      },
      checkEmailExists(email){
        let endpoint = '/api/rest-auth/user/email/';
        apiService(endpoint, "POST", {email: email})
                .then(response => response.json())
                .then(json_response => {
                  if(json_response.message){
                    this.emailErrors = [json_response.message]
                  }else{
                    this.emailErrors = null;
                  }
                })
                .catch(error => console.log(error))
      },
      validateUsername(username){
        if (username.length < 4 || username.length > 15){
          this.usernameErrors = ["Username should be between 5 and 15 symbols "]
        }else{
          this.usernameErrors = null;
          this.checkUserNameExists(username)
        }
      },
      validatePassword(password){
        if (password.length < 8 || password.length > 15){
          this.passwordErrors = ["Password should be between 8 and 15 symbols"]
        }else{
          this.passwordErrors = null;
          console.log("numeric is " + !isNaN(password));
          if (!isNaN(password)){
            this.passwordErrors = ["Password should not be entirely numeric"];
          }else{
            this.passwordErrors = null;
          }
        }
      }
    }
  }
</script>

<style scoped>

</style>