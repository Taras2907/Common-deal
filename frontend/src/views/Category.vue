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
        name: "Category",
        components: {Product},
        props: {
            category: {
                type: String,
                required: true
            }
        },
        data() {
            return {
                products: [],
            }
        },
        methods: {
            loadProducts() {
                let endpoint = `/api/products/?subcategory=${this.category}`;
                apiService(endpoint, 'GET')
                    .then(response => response.json())
                    .then(responseData => {
                        this.products = responseData.results
                    })
                    .catch(error => console.log(error))
            }
        },
        created() {
            this.loadProducts()
        },
        // updated() {
        //     this.loadProducts()
        // }
    }
</script>

<style scoped>

</style>