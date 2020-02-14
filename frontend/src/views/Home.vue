<template>

  <v-row>
    <v-col md="3" sm="6"><Product/></v-col>
    <v-col md="3" sm="6"><Product/></v-col>
    <v-col md="3" sm="6"><Product/></v-col>
    <v-col md="3" sm="6"><Product/></v-col>
    <v-col md="3" sm="6"><Product/></v-col>
  </v-row>

</template>

<script>

import Product from "../components/product_list/Product";
export default {
  components: {Product}
};
</script>
