<template>
    <v-app-bar app
        clipped-left
        color="#FFC107"
        flat>
        <v-img
          class="m-2"
          src="@/assets/logo.png"
          max-width="60"
          max-height="60"
          contain>
        </v-img>

        <v-spacer></v-spacer>

        <v-btn v-if="!isLogged"
          outlined
          :to="'authentication'"
          absolute
          right>Sign In
        </v-btn>

        <Menu v-if="isLogged"/>
      </v-app-bar>
</template>

<script>
    import Menu from "./Menu";
    export default {
        name: "Appbar",
        components: {Menu},
        data() {
            return{
                username: null,
            }
        },
        computed: {
            isLogged: function () {
                return localStorage.username
            }
        },
    }
</script>

<style scoped>
    a {
        text-decoration: none;
    }

</style>