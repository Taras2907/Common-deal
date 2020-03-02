<template>
  <v-row justify="center" class="mb-3">
    <v-col cols="12" sm="10" md="8" lg="10">
      <v-form ref="form" v-model="valid" :lazy-validation="false">
        <v-card>
          <v-card-text elevation="13">
            <v-col cols="12" sm="12" lg="12" class="pb-0">
              <v-text-field
                v-model="username"
                :rules="usernameRules"
                label="Username"
                @input="clearErrors"
                hint="Enter your login"
                :error-messages="errors"
                persistent-hint
                required
              ></v-text-field>
            </v-col>
            <v-col sm="4" lg="4" md="4" offset="8" class="px-0">
              <router-link :to="{ name: 'password-recover' }"
                >Forgot password?</router-link
              >
            </v-col>
            <v-col cols="12" sm="12" lg="12" class="pt-0">
              <v-text-field
                v-model="password"
                :rules="passwordRules"
                label="Password"
                hint="Enter your password"
                persistent-hint
                required
                :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show ? 'text' : 'password'"
                @click:append="show = !show"
              >
              </v-text-field>
            </v-col>
          </v-card-text>
          <v-card-actions>
            <v-btn
              class="w-100 primary"
              :loading="loading"
              :disabled="!valid"
              color="white"
              text
              @click="validate"
              >Login
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-col>
  </v-row>
</template>

<script>
/* eslint-disable */
    import {apiService} from "../common/apiService";

    export default {
        name: "LoginComponent",
        data() {
            return {
                username: null,
                usernameRules: [
                    name => !!name || "Login is required",
                ],
                password: null,
                passwordRules: [
                    password => !!password || "Password is required",
                ],
                errors: null,
                valid: false,
                show: false,
                loading: false,
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
                        if (!responseData.key) {
                            this.errors = responseData.non_field_errors
                        } else {
                            this.$root.$emit('login-user');
                            localStorage.setItem("username", this.username);
                            this.$router.push("/");
                        }
                        this.loading = false
                    })
                    .catch(error => console.log(error))
            },
            validate() {
                if (this.$refs.form.validate()) {
                    this.loading = true;
                    this.loginUser()
                }
            },
            clearErrors() {
                this.errors = null
            }
        }
    }
</script>

<style scoped>

</style>