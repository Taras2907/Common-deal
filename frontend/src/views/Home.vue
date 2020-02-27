<template>

  <v-row>
    <v-col md="3" sm="12" v-for="(product, index) in products" :key="index">
      <Product :product="product"/>
    </v-col>

  </v-row>

</template>

<script>

    import Product from "../components/product_list/Product";
    import {apiService} from "../common/apiService";

    export default {
        components: {Product},
        data() {
            return {
                products: [],
            }
        },
        created() {
            let endpoint = `/api/products/`;
            apiService(endpoint, 'GET')
                .then(response => response.json())
                .then(responseData => {
                    this.products = responseData.results
                })
                .catch(error => console.log(error))
        }
    };
</script>
