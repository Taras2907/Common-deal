<template>
    <v-container>
        <Sorting @sort="sortProducts"></Sorting>
        <v-row>

            <v-col md="3" sm="6" v-for="(product, index) in products" :key="index">
                <router-link :to="{name: 'product-detail', params:{id: product.id}}">
                    <Product :product="product"/>
                </router-link>
            </v-col>

        </v-row>
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
                        console.log(json_response)
                        this.products = json_response.results;
                        this.pages = Math.round(json_response.count / this.productsOnPage);
                    })

            },
            sortProducts(option) {
                console.log(option)
                let sortingOptions = {"Price: Low to High": "-price", "Price: High to Low": "price"};
                let order = sortingOptions[option];
                console.log(order)
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
