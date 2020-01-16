<template>
    <div v-if="emailSent" class="alert alert-success mx-auto" role="alert">
        <p>Account recovery email sent to {{ email }}
        If you don’t see this email in your inbox within 15 minutes, look for it in your junk mail folder. If you find it there, please mark it as “Not Junk”.</p>
    </div>
    <div class="container justify-content-md-center w-25 p-5 border rounded"
         id="main-container"
         v-else
    >
        <div class="container">
            <form @submit.prevent="sendRecoveryEmail(email)">
                <div class="row">
                    <div class="col-12 px-2 ">
                        <p class="text-left border-bottom py-2 border-top">Forgot your account’s password or having trouble logging into your account? Enter your email and we’ll send you a recovery link.</p>
                        <div class="form-group">
                            <div class="text-left pl-2">
                               <label for="registerEmail"><strong>Email</strong></label>
                            </div>

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
                            <p v-if="emailError" class="text-left mt-2">
                                <small class="text-danger row ml-1"
                                  >{{ emailError }}</small
                                >
                            </p>
                        <button v-if="isSending"
                                class="btn btn-primary w-100 mt-5"
                                type="button" disabled>
                            <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
                                Loading...
                        </button>
                        <button v-else
                                :disabled="thereAreNoErrorAndFieldIsNotEmpty"
                                type="submit"
                                class="btn btn-primary w-100 mt-5"
                                id="registerSubmit">
                            Send recovery email
                        </button>

                    </div>
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
    name: "PasswordRecover",
    data(){
        return{
            email: "",
            emailError: null,
            emailSent: false,
            isSending: false,

        }
    },
    computed:{
        thereAreNoErrorAndFieldIsNotEmpty(){
            return this.email === "" || this.emailError
        }
    },
    methods:{
        sendRecoveryEmail(email){
            let endpoint = '/api/rest-auth/password/reset/';
            this.isSending = true;
            apiService(endpoint, "POST", {email: email})
                .then(response => {
                  if (response.status === 200){
                      this.emailSent = true;
                      this.isSending = false;
                  }else{
                      this.emailSent = false;
                      this.isSending = false;
                      console.log("Recovery email wasn't sent")
                  }
                })
                .catch(error => console.log(error))
        },
        checkEmailExists(email){
            let endpoint = '/api/rest-auth/user/email/';
            if (email !== ""){
                apiService(endpoint, "POST", {email: email})
                .then(response => response.json())
                .then(json_response => {
                  if(json_response.response.exists){
                    this.emailError = null;
                  }else{
                    this.emailError = json_response.response.message
                  }
                })
                .catch(error => console.log(error))
            }
        },

    }

}
</script>

<style scoped>

    #main-container {
    margin-top: 7%;
   }
    .alert{
        margin-top: 10%;
        width: 25%;
    }
</style>