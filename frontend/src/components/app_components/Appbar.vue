<template>
  <v-app-bar app clipped-left color="#FFC107" flat>
    <v-app-bar-nav-icon
      class="hidden-lg-and-up"
      @click.stop="toggleDrawer"
    ></v-app-bar-nav-icon>
    <router-link :to="{ name: 'home' }">
      <v-img
        class="m-2"
        src="@/assets/logo.png"
        max-width="60"
        max-height="60"
        contain>
      </v-img>
    </router-link>

    <v-spacer></v-spacer>

    <v-btn
      v-if="!user_logged"
      outlined
      :to="{ name: 'authentication' }"
      absolute
      right
      >Sign In
    </v-btn>

    <Menu v-if="user_logged" />
  </v-app-bar>
</template>

<script>
import Menu from "./Menu";

export default {
  name: "Appbar",
  components: { Menu },
  mounted() {
    this.$root.$on("logout-user", () => {
      this.user_logged = false;
    });
    this.$root.$on("login-user", () => {
      this.user_logged = true;
    });
  },
  data() {
    return {
      username: null,
      user_logged: !!localStorage.username
    };
  },
  methods: {
    toggleDrawer() {
      this.$root.$emit("toggleDrawer");
    }
  }
};
</script>

<style scoped>
a {
  text-decoration: none;
}
</style>
