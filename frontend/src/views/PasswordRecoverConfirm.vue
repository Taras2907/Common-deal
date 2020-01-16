<template>
  <div v-if="passwordSuccessfullyChanged" class="alert alert-success mx-auto" role="alert">
    <p>Password was successfully changed.</p>
    <p>You will be redirected to login page shortly.</p>
  </div>
  <div class="container" v-else>
    <div class="row justify-content-md-center">
      <div class="col-md-5">
        <div class="container p-5 border rounded"
             id="main-container"
        >
          <div class="container">
            <form @submit.prevent="changePassword">
              <div class="row">
                <div class="col-12 px-2 ">
                  <p class="text-left border-bottom py-2 border-top">
                    To finish reset password process fill the new password and confirm password fields.
                  </p>
                  <div class="form-group">
                    <div class="text-left pl-2">
                      <label for="changePassword"><strong>New password</strong></label>
                    </div>
                    <input v-model="password1"
                           @blur="validatePassword(password1)"
                           name="password1"
                           type="password"
                           class="form-control"
                           id="changePassword"
                           placeholder="New password"
                           required
                    />
                    <p v-if="passwordError" class="text-left mt-2">
                      <small class="text-danger row ml-1"
                      >{{ passwordError }}
                      </small>
                    </p>
                    <div class="text-left pl-2 mt-2">
                      <label for="changeConfirmPassword"><strong>Confirm password</strong></label>
                    </div>
                    <input v-model="password2"
                           @blur="checkPasswords"
                           name="password2"
                           type="password"
                           class="form-control"
                           id="changeConfirmPassword"
                           placeholder="Confirm password"
                           required
                    />
                    <p v-if="confirmPasswordError" class="text-left mt-2">
                      <small class="text-danger row ml-1"
                      >Password and confirm password does not match
                      </small
                      >
                    </p>
                    <input type="hidden" v-model="token">
                    <input type="hidden" v-model="uid">
                    <button v-if="isChanging"
                            class="btn btn-primary w-100 mt-5"
                            type="button" disabled>
                      <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
                      Loading...
                    </button>
                    <button v-else
                            :disabled="thereAreErrors || fieldsAreEmpty || !passwordsHaveSameLength"
                            type="submit"
                            class="btn btn-primary w-100 mt-5"
                            id="registerSubmit">
                      Change password
                    </button>

                  </div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
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
        passwordError: null,
        password1: "",
        password2: "",
        confirmPasswordError: null,
        passwordSuccessfullyChanged: false
      }
    },
    computed: {
      fieldsAreEmpty() {
        return this.password1 === "" || this.password2 === ""
      },
      thereAreErrors() {
        return this.confirmPasswordError || this.passwordError !== null
      },
      passwordsHaveSameLength() {
        return this.password1.length === this.password2.length
      }
    },
    methods: {
      validatePassword(password) {
        this.checkPasswords();
        if ((password.length < 7 || password.length > 15) && password !== "") {
          this.passwordError = "Password should be between 8 and 15 symbols"
        } else {
          this.passwordError = null;
          if (!isNaN(password) && password !== "") {
            this.passwordError = "Password should not be entirely numeric";
          } else {
            this.passwordError = null;
          }
        }
      },
      checkPasswords() {
        this.confirmPasswordError =
            ((this.password1 !== this.password2) &&
                this.password1 !== "" &&
                (this.password2 !== ""));
      },
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