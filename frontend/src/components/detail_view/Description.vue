<template>
    <v-container fluid>
        <v-row>
            <v-col :cols="2">
                <ListImageComponent @change-image="changeImage"></ListImageComponent>
            </v-col>
            <v-col :cols="4">
                <v-img max-height="540"
                       max-width="540"
                       :src="`https://frontendcommondeal.blob.core.windows.net/%24web/img/${currentImage}`"></v-img>
                <v-container fluid>
                    <p>{{this.shortDescription}}</p>
                </v-container>
            </v-col>
            <v-col class="productInfo" :cols="6">
                <v-container fluid>
                    <v-row class="priceInfo">
                        <v-card class="cardInfo"
                                :elevation="5"
                                height="80"
                                width="670"
                        >
                            <h3>Time to end of a deal: </h3>
                            <h3 >{{this.expirationDate}}</h3>
                        </v-card>
                    </v-row>
                </v-container>
                <v-container fluid>
                    <v-row class="priceInfo">
                        <v-card class="cardInfo"
                                :elevation="5"
                                height="250"
                                width="670"
                        >

                            <v-row class="row mx-1">
                                <v-col :cols="4">
                                    <v-card class="text">
                                        <p>${{this.product.price}}</p>
                                    </v-card>
                                </v-col>
                                <v-col :cols="4">

                                    <v-btn class="button" @click="isSubscribed = ! isSubscribed" x-large color="success"
                                           dark>
                                        <p v-if="isSubscribed">Unsubscribe</p>
                                        <p v-else>Subscribe</p>
                                    </v-btn>


                                </v-col>
                                <v-col :cols="4">
                                    <v-btn class="button" @click="isLiked = ! isLiked"
                                           :outlined="isLiked"
                                           x-large color="success" dark>
                                        <v-icon class="button">mdi-heart</v-icon>
                                    </v-btn>

                                </v-col>

                            </v-row>
                            <v-divider></v-divider>
                            <v-row class="mt-6"
                                   justify="center">
                                <v-col :cols="8">
                                    <h2>The seller of this product is {{this.product.seller}}</h2>
                                </v-col>

                            </v-row>
                        </v-card>
                    </v-row>
                </v-container>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    /* eslint-disable */
    import ListImageComponent from "./ListImageComponent";

    export default {
        name: "Description",
        components: {ListImageComponent},
        props: {
            product: {
                type: Object,
                required: true,
            },
            shortDescription: {
                type: String,
                required: true,
            },
            expirationDate: {
                type: String,
                required: true,
            }
        },
        data() {
            return {
                isSubscribed: false,
                isLiked: true,
                currentImage: "asus2.jpeg",

            }
        },
        methods: {
            changeImage(image) {
                this.currentImage = image
            },

        },
    }
</script>

<style scoped>
    .productInfo {
        background: #ECEFF1
    }

    .priceInfo {
        margin-left: auto;
        margin-right: auto;
        margin-top: auto;
    }

    .cardInfo {
        margin-left: auto;
        margin-right: auto;
    }

    h3, h2 {
        text-align: center;
        font-size: 2vw;
        max-width: 100%;
        max-height: 100%;

    }

    p {
        font-size: 1vw;
    }

    .text {
        text-align: center;
        height: 51px;
        margin-top: auto;
    }

    .text > p {
        padding-top: 10px;
        background-color: #FFE0B2;
        color: #FF7043;
        height: 100%;
        width: 100%;
        margin-bottom: 0;
    }

    .button {
        height: 100%;
        width: 100%;
        max-width: 100%;
        max-height: 100%;
        min-width: unset !important;

    }

    .row {
        max-width: 100%;
        max-height: 100%;
    }

    /*@media screen and (min-width: 601px) {*/
    /*    .button {*/
    /*        font-size: 20px;*/
    /*    }*/
    /*}*/

    /*@media screen and (max-width: 600px) {*/
    /*    .button  {*/
    /*        font-size: 10px;*/
    /*    }*/
    /*}*/
</style>