<template>
    <v-card color="basil">
        <v-card-title class="text-center justify-center py-6">
            <h3 class="font-weight-bold basil--text">{{this.product.name}}</h3>
        </v-card-title>

        <v-tabs
                v-model="tab"
                background-color="transparent"
                color="basil"
                grow
                show-arrows
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
                    <Description v-if="product != null" :product="product"
                                 :shortDescription="shortDescription"
                                 :expirationDate="expirationDate"
                    ></Description>
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
                                            <v-col col="6" sm="6">
                                                <span class="pl-5">{{key}}</span>
                                            </v-col>

                                            <v-col col="6" sm="6">
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
                <Reviews></Reviews>
            </v-tab-item>
            <v-tab-item :key="4">
                <Shipping></Shipping>
            </v-tab-item>

        </v-tabs-items>
    </v-card>
</template>

<script>
    /* eslint-disable */
    import Description from "../components/detail_view/Description";
    import {apiService} from "../common/apiService";
    import Shipping from "../components/detail_view/Shipping";
    import Reviews from "../components/detail_view/Reviews";

    export default {
        name: "Tab",
        props: {
            id: {
                type: String,
                required: true,
            }
        },
        components: {Reviews, Shipping, Description},
        data() {
            return {
                tab: null,
                product: {},
                shortDescription: "",
                expirationDate: "",
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
                        this.setTimer(json_response.expiration_date);
                        this.createShortDescription();
                    })
            },
            createShortDescription() {
                let description = "";
                for (let [key, value] of Object.entries(this.product.attributes)) {
                    description += key + "-" + value + "/";
                }
                this.shortDescription = description
            },
            setTimer(date) {
                let countDownDate = new Date(date).getTime();
                let x = setInterval(() => {
                    let now = new Date().getTime();

                    let distance = countDownDate - now;

                    let days = Math.floor(distance / (1000 * 60 * 60 * 24));
                    let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                    let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                    let seconds = Math.floor((distance % (1000 * 60)) / 1000);
                    this.expirationDate = days + "d " + hours + "h "
                        + minutes + "m " + seconds + "s ";
                    if (distance < 0) {
                        clearInterval(x);
                        this.expirationDate = "EXPIRED";
                    }

                }, 1000);
            }
        },
        created() {
            this.getProductData()
        }
    }
</script>

<style scoped>
</style>