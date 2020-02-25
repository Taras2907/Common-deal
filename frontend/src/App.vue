<template>

  <v-app>
    <Appbar/>

    <Drawer v-if="['authentication'].indexOf($route.name) === -1"/>

    <v-content>

      <v-container>
          <router-view></router-view>
      </v-container>
    </v-content>

    <Footer/>

  </v-app>

</template>

<script>

import Appbar from "./components/app_components/Appbar";
import Drawer from "./components/app_components/Drawer";
import Footer from "./components/app_components/Footer";
export default {
  name: "App",
    components: {Footer, Drawer, Appbar},
    data: () => ({
      user_logged: false,
  })
};
</script>
