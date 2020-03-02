<template>
  <v-container class="mt-1">
    <v-container fluid v-if="emailSent" class="mx-auto">
      <v-alert type="success" max-width="600px" class="mx-auto">
        <p>
          Account recovery email sent to {{ email }} If you don’t see this email
          in your inbox within 15 minutes, look for it in your junk mail folder.
          If you find it there, please mark it as “Not Junk”.
        </p>
      </v-alert>
    </v-container>
    <v-row justify="center" v-else>
      <v-form ref="form" v-model="valid" :lazy-validation="false">
        <v-card max-width="400px">
          <v-card-text>
            <v-col cols="12">
              <p class="text">
                Forgot your account’s password or having trouble logging into
                your account? Enter your email and we’ll send you a recovery
                link.
              </p>
            </v-col>
            <v-divider class="my-1"></v-divider>
            <v-col cols="12" class="py-0">
              <v-text-field
                v-model="email"
                :rules="emailRules"
                label="Email"
                hint="Enter your email"
                persistent-hint
                required
              ></v-text-field>
            </v-col>
          </v-card-text>
          <v-card-actions>
            <v-btn
              class="w-100 primary"
              :loading="isSending"
              :disabled="!valid"
              color="white"
              text
              @click="validate"
              >Send recover email
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
        name: "PasswordRecover",
        data() {
            return {
                email: "",
                emailRules: [
                    email => !!email || "Email is required",
                    email => /.+@.+\..+/.test(email) || 'E-mail must be valid',

                ],
                emailSent: false,
                isSending: false,
                valid: false,

            }
        },
        methods: {
            sendRecoveryEmail(email) {
                let endpoint = '/api/rest-auth/password/reset/';
                this.isSending = true;
                apiService(endpoint, "POST", {email: email})
                    .then(response => {
                        if (response.status === 200) {
                            this.emailSent = true;
                            this.isSending = false;
                        } else {
                            this.emailSent = false;
                            this.isSending = false;
                            console.log("Recovery email wasn't sent")
                        }
                    })
                    .catch(error => console.log(error))
            },
            checkEmailExists(email) {
                let endpoint = '/api/rest-auth/user/email/';
                if (email !== "") {
                    apiService(endpoint, "POST", {email: email})
                        .then(response => response.json())
                        .then(json_response => {
                            if (json_response.response.exists) {
                                this.emailError = null;
                            } else {
                                this.emailError = json_response.response.message
                            }
                        })
                        .catch(error => console.log(error))
                }
            },
            validate() {
                if (this.$refs.form.validate()) {
                    this.isSending = true;
                    this.sendRecoveryEmail(this.email)
                }
            },

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