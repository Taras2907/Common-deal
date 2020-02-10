<template>
  <div class="container-fluid h-100">
    <Products></Products>
  </div>
</template>

<script>
  // @ is an alias to /src

  import Products from "../components/Products";
  export default {
    name: "home",
    components: {Products},
  };
</script>
