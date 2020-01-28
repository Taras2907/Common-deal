<template>
  <div class="container">
    <div class="row justify-content-md-center">
      <div class="col-md-5">
        <div class="container p-5 border rounded"
             id="main-container">
          <ul
                  class="nav bg-light nav-pills rounded nav-fill mb-3"
                  id="pills-tab"
                  role="tablist"
          >
            <li class="nav-item">
              <a
                      class="nav-link active"
                      id="pills-home-tab"
                      data-toggle="pill"
                      href="#login"
                      role="tab"
                      aria-controls="pills-home"
                      aria-selected="true"
              >Login</a
              >
            </li>
            <li class="nav-item">
              <a
                      class="nav-link"
                      id="pills-profile-tab"
                      data-toggle="pill"
                      href="#registration"
                      role="tab"
                      aria-controls="pills-profile"
                      aria-selected="false"
              >Registration</a
              >
            </li>
          </ul>
          <div class="tab-content" id="pills-tabContent">
            <LoginComponent></LoginComponent>
            <RegistrationComponent @switch-tab="switchToLogin"></RegistrationComponent>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  /* eslint-disable */
  import RegistrationComponent from "@/components/Registration";
  import LoginComponent from "../components/Login";

  export default {
    name: "Authentication",
    components: {LoginComponent, RegistrationComponent},
    methods:{
        switchToLogin(){
            let registrationTab = document.querySelector("#pills-home-tab");
            registrationTab.click();
        }
    }
  }
</script>

<style scoped>
  #main-container {
    margin-top: 7%;
  }
</style>