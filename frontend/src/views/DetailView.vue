<template>
    <v-card color="basil">
        <v-card-title class="text-center justify-center py-6">
            <h3 class="font-weight-bold display-3 basil--text">{{this.product.name}}</h3>
        </v-card-title>

        <v-tabs
                v-model="tab"
                background-color="transparent"
                color="basil"
                grow
        >
            <v-tab
                    v-for="item in items"
                    :key="item.id"
            >
                {{ item.name }}
            </v-tab>
        </v-tabs>

        <v-tabs-items v-model="tab" class="image">
            <v-tab-item :key="1">
                <v-card
                        color="basil"
                        flat
                >
                    <Description v-if="product != null" :product="product" :shortDescription="shortDescription"></Description>
                </v-card>
            </v-tab-item>
            <v-tab-item :key="2">
                <v-card
                        color="basil"
                        flat
                >
                    <v-list>
                        <v-card class="card">
                            <v-list-item v-for="(value, key) in product.attributes" :key="key">
                                <v-list-item-content>
                                    <v-list-item-title>
                                        <v-row>
                                            <v-col :col="1">
                                                <span class="pl-5">{{key}}</span>
                                            </v-col>

                                            <v-col :col="2">
                                                <span>{{value}}</span>
                                            </v-col>
                                        </v-row>
                                    </v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </v-card>
                    </v-list>
                </v-card>
            </v-tab-item>
            <v-tab-item :key="3">
                <h1>reviews</h1>
            </v-tab-item>
            <v-tab-item :key="4">
                <v-card>
                    <v-container class="pl-12" fluid>
                        <h2>Checkout</h2>
                        <p>Please note: all the rights provided for in the Law "On Protection of Consumer Rights" apply
                            to
                            buyers of our store.</p>
                        <p>
                            You can place an order in two ways:
                        </p>
                        <ul>
                            <li>
                                a) using the "Subscribe" directly in the store (the method is described below)
                            </li>
                            <li>
                                b) by phone.
                            </li>
                        </ul>
                        <p>Ordering using the "Subscribe" allows you to fully control the process. By entering your
                            e-mail and password that you selected during registration you will get access to the status
                            of
                            your order. You will be able to control our receipt of payment, sending the order to you,
                            the
                            date of receipt of the order, the history of all previous orders.</p>
                        <h2>Delivery</h2>
                        <h2>Warranty</h2>
                        <p>
                            For all products sold in our store, a guarantee is provided from 2 weeks to 120 months,
                            depending on the manufacturer's service policy. The warranty period is indicated in the
                            description of each product on our website. The warranty certificate is confirmed by the
                            manufacturer's warranty card, or the warranty card "Common Deal - online paltform".
                        </p>
                        <p>
                            Checking the completeness and absence of defects in the product is carried out during the
                            transfer of goods to the buyer. The completeness of the product is determined by the
                            description
                            of the product or the manual for its operation.
                        </p>
                        <h3>Exchange and return of goods within the first 14 days after purchase.</h3>
                        <p>

                            In accordance with the "Law on the Protection of Consumer Rights", buyers of our store have
                            the right to exchange or return the goods purchased from us within the first 14 days after
                            purchase.
                            Please note - only new goods that were not in use and have no signs of use are subject to
                            exchange or return: scratches, chips, scuffs, on the phone’s meter for no more than 5
                            minutes of calls, the software has not been changed, etc.
                            And also should be saved:
                        </p>
                        <ul>
                            <li>full set of goods;</li>
                            <li>integrity and all packaging components;</li>
                            <li>label</li>
                            <li>factory marking</li>
                        </ul>
                    </v-container>


                </v-card>
            </v-tab-item>

        </v-tabs-items>
    </v-card>
</template>

<script>
    /* eslint-disable */
    import Description from "../components/detail_view/Description";
    import {apiService} from "../common/apiService";

    export default {
        name: "Tab",
        props: {
            id: {
                type: String,
                required: true,
            }
        },
        components: {Description},
        data() {
            return {
                tab: null,
                product: {},
                shortDescription: "",
                items: [
                    {
                        id: 1,
                        name: 'Item description',
                    },
                    {
                        id: 2,
                        name: 'Characteristics',
                    },
                    {
                        id: 3,
                        name: 'Reviews',
                    },
                    {
                        id: 4,
                        name: 'Shipping',
                    },
                ],
            }
        },
        methods: {
            getProductData() {
                let endpoint = `/api/products/${this.id}/`;
                apiService(endpoint)
                    .then(response => response.json())
                    .then(json_response => {
                        this.product = json_response;
                        this.createShortDescription();
                    })
            },
            createShortDescription(){
                let description = "";
                for (let [key, value] of Object.entries(this.product.attributes) ){
                    description += key + "/" + value + "/";
                }
                this.shortDescription = description
            },
        },
        created() {
            this.getProductData()
        }
    }
</script>

<style scoped>
</style>