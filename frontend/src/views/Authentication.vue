<template>
  <v-card tile class="d-flex mx-auto" max-width="600px" max-height="700px">
    <v-tabs centered v-model="tab" fixed-tabs>
      <v-tab key="login">Login</v-tab>
      <v-tab key="registration">Registration</v-tab>

      <v-tab-item key="login">
        <LoginComponent></LoginComponent>
      </v-tab-item>

      <v-tab-item key="registration">
        <RegistrationComponent
          @switch-tab="switchToLogin"
        ></RegistrationComponent>
      </v-tab-item>
    </v-tabs>
  </v-card>
</template>

<script>
/* eslint-disable */
    import RegistrationComponent from "@/components/Registration";
    import LoginComponent from "../components/Login";

    export default {
        name: "Authentication",
        components: {LoginComponent, RegistrationComponent},
        data() {
            return {
                tab: null,
            }
        },
        methods: {
            switchToLogin(){
                this.tab = 0;
            }
        }
    }
</script>

<style scoped>
</style>