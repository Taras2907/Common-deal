<template>



</template>

<script>
    import {apiService} from "../common/apiService";

    export default {
        name: "Products",
        data() {
            return {
                products: [],
                isLoading: false,
                currentOrder: "-id",
                productsOnPage: 8,
                pages: null,
                sortOption: "Price: Low to High",
                currentPage: 1
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
                        console.log(json_response.results)
                    })

            },
            sortProducts(option) {
                let sortingOptions = {"Price: Low to High": "-price", "Price: High to Low": "price"};
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
            let firstPage = 1;
            this.getProducts(this.currentOrder, firstPage)
        }
    }
</script>

<style scoped>
    .pagination {
        margin-right: auto;
    }

    .fill-height {
        min-height: 100%;
        height: 100%;
    }
</style>