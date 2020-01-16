<template>
  <div
          class="container tab-pane fade show active"
          id="login"
          role="tabpanel"
          aria-labelledby="pills-home-tab"
  >
    <form @submit.prevent="loginUser">
      <div class="form-group">
        <label for="loginUserEmail">Enter Username</label>
        <input
                v-model="username"
                name="userEmail"
                type="text"
                class="form-control"
                id="loginUserEmail"
                aria-describedby="loginHelp"
                placeholder="Username"
                required
        />
        <div v-if="errors">
          <p class="text-left mt-2">
            <small
                    class="text-danger row ml-1"
                    v-for="(message, index) in errors"
                    :key="index"
            >{{ message }}
            </small
            >
          </p>
        </div>
        <small v-else id="loginHelp" class="form-text text-muted"
        >Fill the form and press submit to create account
        </small>
      </div>
      <div class="form-group">
        <div class="row-no-gutters px-0 mx-0 text-left">
                <label class="col-sm-6 text-left pl-2" for="loginPassword">Password</label>
                <router-link class="col-sm-6 text-left pl-2"
                             :to="{name: 'password-recover'}"
                >Forgot password?</router-link>
        </div>
        <input
                v-model="password"
                name="password"
                type="password"
                class="form-control"
                id="loginPassword"
                placeholder="Password"
                autocomplete="off"
                required
        />
      </div>
      <button
              :disabled="fieldsAreEmpty"
              type="submit"
              class="btn btn-primary"
              id="loginSubmit">
        Submit
      </button>
    </form>

  </div>
</template>

<script>
  /* eslint-disable */
  import {apiService} from "../common/apiService";

  export default {
    name: "LoginComponent",
    data() {
      return {
        username: null,
        password: null,
        errors: null,
      }
    },
    computed: {
      fieldsAreEmpty() {
        return (this.username === null || this.username === "")
            || (this.password === null || this.password === "");
      }
    },
    methods: {
      loginUser() {
        let endpoint = `/api/rest-auth/login/`;
        let data = {
          username: this.username,
          password: this.password
        };
        apiService(endpoint, 'POST', data)
            .then(response => response.json())
            .then(responseData => {
              console.log(responseData);
              if (!responseData.key) {
                this.applyErrors(responseData)
              } else {
                this.errors = null;
                localStorage.setItem("username", this.username)
              }
            })
            .catch(error => console.log(error))
      },
      applyErrors(responseData) {
        if (responseData.non_field_errors) {
          this.errors = responseData.non_field_errors
        }
      }
    }
  }
</script>

<style scoped>

</style>