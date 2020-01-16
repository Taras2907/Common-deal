<template>
  <div class="bg">
    <div class="container mt-3">
      <router-link :to="{ name: 'home' }"
      ><img src="../assets/dribbble-helio-404.gif" alt="Page not found"
      /></router-link>
    </div>
  </div>
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
