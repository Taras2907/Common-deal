<template>
  <v-container>
    <Sorting @sort="sortProducts"></Sorting>
    <v-row>
      <v-col
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
  </v-container>
</template>

<script>
import Product from "../components/product_list/Product";
import Sorting from "../components/product_list/Sorting";

import { apiService } from "../common/apiService";

export default {
  name: "Category",
  components: { Product, Sorting },
  props: {
    category: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      products: [],
      isLoading: false,
      currentOrder: "-id",
      productsOnPage: 8,
      sortOption: "Price: Low to High",
      currentPage: 1
    };
  },
  methods: {
    loadProducts(order, page) {
      let endpoint = `/api/products/?subcategory=${this.category}&orderby=${order}&page=${page}`;
      apiService(endpoint, "GET")
        .then(response => response.json())
        .then(responseData => {
          this.products = responseData.results;
        })
        .catch(error => console.log(error));
    },
    sortProducts(option) {
      let sortingOptions = {
        "Price: Low to High": "price",
        "Price: High to Low": "-price"
      };
      let order = sortingOptions[option];
      this.currentOrder = order;
      this.loadProducts(order, this.currentPage);
    }
  },
  created() {
    this.loadProducts(this.currentOrder, this.currentPage);
  }
};
</script>

<style scoped></style>
