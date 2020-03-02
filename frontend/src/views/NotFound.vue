<template>
  <v-container fluid>
    <router-link :to="{ name: 'home' }">
      <v-img
        contain
        aspect-ratio="1"
        src="../assets/page_not_found.gif"
      ></v-img>
    </router-link>
  </v-container>
</template>

<script>
export default {
  name: "NotFound",
  data() {
    return {
      message: "404 - Page Not Found"
    };
  }
};
</script>

<style>
.bg {
  /*background-image: url('../assets/dribbble-helio-404.gif');*/
  /*background-repeat: no-repeat;*/
  /*background-size: 100% 100%;*/
  position: fixed;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
}

.bg img {
  position: absolute;
  top: 0;
  bottom: 0;
  right: 0;
  left: 0;
  margin: auto;
  min-width: 50%;
  min-height: 50%;
}

/*html{*/
/*    height: 100%;*/
/*}*/
</style>
