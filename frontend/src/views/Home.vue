<template>

  <v-row>
    <v-col md="3" sm="6" v-for="(product, index) in products.results" :key="index">
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
                products: null,
            }
        },
        created() {
            let endpoint = `/api/products/`;
            apiService(endpoint, 'GET')
                .then(response => response.json())
                .then(responseData => {
                    this.products = responseData
                })
                .catch(error => console.log(error))
        }
    };
</script>
