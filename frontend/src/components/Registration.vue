<template>
  <v-row justify="center" class="mb-2">
    <v-col cols="12" sm="10" md="8" lg="10">
      <v-form ref="form" v-model="valid" :lazy-validation="false">
        <v-card>
          <v-card-text>
            <v-col cols="12" sm="12" lg="12">
              <v-text-field
                v-model="username"
                @input="usernameErrors = null"
                @blur="checkUserNameExists"
                :error-messages="usernameErrors"
                :loading="usernameChecking"
                :rules="[
                  usernameRules.nameIsRequired,
                  usernameRules.nameLenBiggerThan5Chars,
                  usernameRules.nameContainsLettersAndDigits
                ]"
                label="Username"
                hint="Username should be at least 5 characters long and contain only letters and digits"
                persistent-hint
                required
              ></v-text-field>
            </v-col>

            <v-col cols="12" sm="12" lg="12">
              <v-text-field
                v-model="password1"
                :rules="passwordRules"
                label="Password"
                hint="Eight characters sequence with at least 1 capital letter and 1 digit"
                persistent-hint
                required
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show1 ? 'text' : 'password'"
                counter
                loading
                @click:append="show1 = !show1"
              >
                <template v-slot:progress>
                  <v-progress-linear
                    :value="progress"
                    :color="color"
                    absolute
                    height="2"
                  ></v-progress-linear>
                </template>
              </v-text-field>
            </v-col>

            <v-col cols="12" sm="12" lg="12">
              <v-text-field
                v-model="password2"
                :rules="password2Rules"
                label="Confirm password"
                hint="Repeat your password"
                persistent-hint
                required
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show2 ? 'text' : 'password'"
                counter
                @click:append="show2 = !show2"
              ></v-text-field>
            </v-col>
            <v-col cols="12" sm="12" lg="12">
              <v-text-field
                @blur="checkEmailExists"
                @input="emailErrors = null"
                :error-messages="emailErrors"
                v-model="email"
                :rules="[
                  emailRules.emailPatternIsValid,
                  emailRules.emailRequired
                ]"
                label="Email"
                hint="Enter your email"
                persistent-hint
                required
                :loading="emailChecking"
              ></v-text-field>
            </v-col>
          </v-card-text>

          <v-card-actions>
            <v-btn
              class="w-100 primary"
              :loading="isRegistering"
              color="white"
              :disabled="false"
              text
              @click="validate"
              >Register
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
        name: "RegistrationComponent",
        data() {
            return {
                username: "",
                usernameRules: {
                    nameIsRequired: name => !!name || "Username is required",
                    nameLenBiggerThan5Chars: name => (name && name.length > 4) || "Username should be not less than 5 characters",
                    nameContainsLettersAndDigits: name => /^([a-z]|[A-Z]|[0-9])*$/.test(name) || "Username should contain only letters and digits", // . _ -
                },
                usernameChecking: false,

                password1: "",
                passwordRules: [
                    password => !!password || "Password is required",
                    password => (password && (password.length > 7 && password.length < 16)) || "Password should be not less than 8 characters and not bigger than 15",
                    password => /^([a-z]|[A-Z]|[0-9])*$/.test(password) || "Password should contain only letters and digits",

                ],
                show1: false,

                password2: "",
                password2Rules: [
                    password => (password && password === this.password1) || "Password are not equal",
                ],
                show2: false,

                email: null,
                emailRules: {
                    emailRequired: email => !!email || "email is required",
                    emailPatternIsValid: email => /.+@.+\..+/.test(email) || 'E-mail must be valid',
                },
                isRegistering: false,
                usernameErrors: null,
                passwordErrors: null,
                emailErrors: null,
                emailChecking: false,
                valid: false,
            }
        },
        computed: {
            progress() {
                return Math.min(100, this.password1.length * 12.5) // 12.5 * 8 chars = 100% progress
            },
            color() {
                let hasOneCapitalLetter = p => /[A-Z]/.test(p) ? 1 : 0;
                let hasOneDigit = p => /[0-9]/.test(p) ? 1 : 0;
                let has8charsLen = p => p.length > 7 ? 1 : 0;
                let theColor = hasOneCapitalLetter(this.password1) +
                    hasOneDigit(this.password1) +
                    has8charsLen(this.password1);
                let colors = {0: 'error', 1: 'error', 2: 'warning', 3: 'success'};
                return colors[theColor]
            },
            usernameIsValid() {
                let rules = this.usernameRules;
                return rules.nameContainsLettersAndDigits(this.username) &&
                    rules.nameIsRequired(this.username) &&
                    rules.nameLenBiggerThan5Chars(this.username)
            },
            emailIsValid() {
                let rules = this.emailRules;
                return rules.emailRequired(this.email) &&
                    rules.emailPatternIsValid(this.email)
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
                        } else {
                            this.$emit('switch-tab');
                            location.reload();
                            // this.username = '';
                            // this.password1 = '';
                            // this.password2 = '';
                            // this.email = '';

                        }
                    })
                    .catch(error => console.log(error))
            }
            ,
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
            checkUserNameExists() {
                if (this.usernameIsValid === true) {

                    let endpoint = '/api/rest-auth/user/name/';
                    this.usernameChecking = true;

                    apiService(endpoint, "POST", {username: this.username})
                        .then(response => response.json())
                        .then(json_response => {
                            setTimeout(() => {

                                this.usernameChecking = false;
                                if (json_response.message) {
                                    this.usernameErrors = [json_response.message]
                                } else {
                                    this.usernameErrors = null;
                                }

                            }, 1000)
                        })
                        .catch(error => console.log(error))
                }
            }
            ,
            checkEmailExists() {
                if (this.emailIsValid === true) {
                    let endpoint = '/api/rest-auth/user/email/';
                    this.emailChecking = true;
                    apiService(endpoint, "POST", {email: this.email})
                        .then(response => response.json())
                        .then(json_response => {
                            setTimeout(() => {
                                this.emailChecking = false;
                                if (json_response.response.exists) {
                                    this.emailErrors = [json_response.response.message]
                                } else {
                                    this.emailErrors = null
                                }

                            }, 1000);


                        })
                        .catch(error => console.log(error))
                }


            }
            ,
            validate() {
                if (this.$refs.form.validate()) {
                    this.registerUser()
                }
            }
        }
    }
</script>

<style scoped>

</style>