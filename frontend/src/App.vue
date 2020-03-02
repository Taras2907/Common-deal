<template>
  <v-app>
    <Appbar />

    <Drawer v-if="!sideBarMustBeShown" />

    <v-content>
      <v-container>
        <router-view :key="$route.fullPath"></router-view>
      </v-container>
    </v-content>

    <Footer />
  </v-app>
</template>

<script>
import Appbar from "./components/app_components/Appbar";
import Drawer from "./components/app_components/Drawer";
import Footer from "./components/app_components/Footer";

export default {
  name: "App",
  components: { Footer, Drawer, Appbar },
  data: () => ({
    user_logged: false
  }),
  computed: {
    sideBarMustBeShown() {
      return (
        this.$route.name === "password-recover" ||
        this.$route.name === "password-recover-confirm" ||
        this.$route.name === "authentication" ||
        this.$route.name === "page-not-found"
      );
    }
  }
};
</script>
