<template>
  <v-row justify="center">
    <v-col lg="4" sm="6" class="p-0 text-center">
      <v-select
        @change="triggerSortOrder(sortOption)"
        v-model="sortOption"
        :items="items"
        label="Low to High"
        dense
        solo
      ></v-select>
    </v-col>
  </v-row>
</template>

<script>
/* eslint-disable */

    import {apiService} from "../../common/apiService.js";

    export default {
        name: "Products",
        data() {
            return {
                isLoading: false,
                currentOrder: "-id",
                productsOnPage: 8,
                pages: null,
                sortOption: "Price: Low to High",
                currentPage: 1,
                items: ['Price: Low to High', 'Price: High to Low'],

            }
        },
        methods: {
            triggerSortOrder(sortOrder) {
                this.$emit('sort', sortOrder)
            }
        }
    }
</script>

<style scoped>

</style>