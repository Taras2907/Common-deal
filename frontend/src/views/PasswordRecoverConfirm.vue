<template>
  <v-container class="mt-1">
    <v-container fluid v-if="passwordSuccessfullyChanged" class="mx-auto mt-4">
      <v-alert type="success" max-width="600px" class="mx-auto">
        <p class="text">
          Password was successfully changed. You will be redirected to login
          page shortly.
        </p>
      </v-alert>
    </v-container>
    <v-row justify="center" v-else>
      <v-form ref="form" v-model="valid" :lazy-validation="false">
        <v-card max-width="400px">
          <v-card-text>
            <v-col cols="12">
              <p class="text">
                To finish reset password process fill the new password and
                confirm password fields.
              </p>
            </v-col>
            <v-divider class="my-1"></v-divider>
            <v-col cols="12" class="py-0">
              <v-text-field
                v-model="password1"
                :rules="password1Rules"
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
            <v-col cols="12" class="py-0">
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
          </v-card-text>
          <v-card-actions>
            <v-btn
              class="w-100 primary"
              :loading="isChanging"
              :disabled="!valid"
              color="white"
              text
              @click="validate"
              >Change password
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-form>
    </v-row>
  </v-container>
</template>

<script>
/* eslint-disable */
    import {apiService} from "../common/apiService";

    export default {
        name: "PasswordRecoverConfirm",
        props: {
            uid: {
                type: String,
                required: true
            },
            token: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                isChanging: false,
                valid: false,
                password1: "",
                password1Rules: [
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
                confirmPasswordError: null,
                passwordSuccessfullyChanged: false
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
        },
        methods: {
            changePassword() {
                let endpoint = `/api/rest-auth/password/reset/confirm/${this.uid}/${this.token}/`;
                let data = {
                    uid: this.uid,
                    token: this.token,
                    new_password1: this.password1,
                    new_password2: this.password2
                };
                this.isChanging = true;
                apiService(endpoint, "POST", data)
                    .then(response => {
                        if (response.status === 200) {
                            this.isChanging = false;
                            this.passwordSuccessfullyChanged = true;
                            setTimeout(() => {
                                this.$router.push('/authentication')
                            }, 5000);


                        } else {
                            this.isChanging = false;
                        }
                    })

                    .catch(error => console.log(error))
            },
            validate() {
                if (this.$refs.form.validate()) {
                    this.isChanging = true;
                    this.changePassword()
                }
            },
        },
        created() {
            console.log(this.uid, this.token)
        }

    }
</script>


<style scoped>
    #main-container {
        margin-top: 7%;
    }

    .alert {
        margin-top: 10%;
        width: 25%;
    }

</style>