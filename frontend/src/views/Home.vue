<template>
  <v-container v-show="!isLoading">
    <Sorting @sort="sortProducts"></Sorting>
    <v-row>
      <v-col
        class="p-1"
        md="4"
        sm="6"
        cols="12"
        v-for="(product, index) in products"
        :key="index"
      >
        <router-link
          :to="{ name: 'product-detail', params: { id: product.id } }"
        >
          <Product :product="product" />
        </router-link>
      </v-col>
    </v-row>
    <div class="text-center">
      <v-overlay :value="isLoading">
        <v-progress-circular indeterminate color="amber"></v-progress-circular>
      </v-overlay>
    </div>
  </v-container>
</template>

<script>
/* eslint-disable */

    import Product from "../components/product_list/Product";
    import Sorting from "../components/product_list/Sorting";
    import {apiService} from "../common/apiService";

    export default {
        components: {Product, Sorting},
        data() {
            return {
                products: [],
                isLoading: false,
                currentOrder: "-id",
                productsOnPage: 8,
                pages: null,
                sortOption: "Price: Low to High",
                currentPage: 1,
            }
        },
        methods: {
            getProducts(order, page) {
                let endpoint = `/api/products/?orderby=${order}&page=${page}`;
                this.isLoading = true;
                apiService(endpoint, "GET")
                    .then(response => response.json())
                    .then(json_response => {
                        this.products = json_response.results;
                        this.pages = Math.round(json_response.count / this.productsOnPage);
                        this.isLoading = false;

                    })

            },
            sortProducts(option) {
                let sortingOptions = {"Price: Low to High": "price", "Price: High to Low": "-price"};
                let order = sortingOptions[option];
                this.currentOrder = order;
                this.getProducts(order, this.currentPage)
            },
            changePage(pageNumber) {
                this.currentPage = pageNumber;
                this.getProducts(this.currentOrder, pageNumber)
            }

        },
        created() {
            this.getProducts(this.currentOrder, this.currentPage)
        }
    };
</script>
