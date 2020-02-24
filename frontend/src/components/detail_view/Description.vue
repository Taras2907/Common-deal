<template>
    <v-row class="mx-0 px-0">
        <v-col cols="2" class="pt-0 pr-0 pl-6">
            <ListImageComponent @change-image="changeImage"></ListImageComponent>
        </v-col>
        <v-col cols="4">
            <v-img max-height="540"
                   max-width="540"
                   :lazy-src="`https://frontendcommondeal.blob.core.windows.net/%24web/img/${currentImage}`"
                   :src="`https://frontendcommondeal.blob.core.windows.net/%24web/img/${currentImage}`"></v-img>
            <v-container fluid>
                <p>{{this.shortDescription}}</p>
            </v-container>
        </v-col>
        <v-col class="productInfo" cols="6">
            <v-card class="mb-3"
                    :elevation="5"
                    height="80"
                    width="670"
            >
                <v-card-text>
                    <v-container fluid class="my-0 py-0">
                        <p class="headers pb-lg-2 pb-sm-0">Time to end of a deal: </p>
                        <p class="headers">{{this.expirationDate}}</p>
                    </v-container>

                </v-card-text>
            </v-card>
                <v-card class="cardInfo"
                        :elevation="5"
                        height="250"
                        width="670"
                >

                    <v-row class="row mx-1 px-0">
                        <v-col cols="4" class="px-1">
                            <v-card class="text">
                                <p>${{this.product.price}}</p>
                            </v-card>
                        </v-col>
                        <v-col cols="4" class="px-1">

                            <v-btn class="button p-0"
                                   @click="toggleModal"
                                   x-large color="success"
                                   :outlined="isSubscribed"
                                   dark>
                                <p v-if="isSubscribed">Unsubscribe</p>
                                <p v-else>Subscribe</p>
                            </v-btn>
                            <Dialog :dialog="dialog"
                                    @close-modal="toggleModal"
                                    @subscribe="subscribeUser"
                            ></Dialog>


                        </v-col>
                        <v-col cols="4" class="px-1">
                            <v-btn class="button p-0" @click="isLiked = ! isLiked"
                                   :outlined="isLiked"
                                   x-large color="success" dark>
                                <v-icon class="button">mdi-heart</v-icon>
                            </v-btn>

                        </v-col>

                    </v-row>
                    <v-divider></v-divider>
                        <v-col cols="12">
                            <p class="headers">The seller of this product is {{this.product.seller}}</p>
                        </v-col>
                </v-card>
        </v-col>
        <div class="text-center">
            <v-overlay :value="overlay">
                <v-progress-circular
                        indeterminate
                        color="amber"
                ></v-progress-circular>
            </v-overlay>

        </div>
    </v-row>


</template>

<script>
    /* eslint-disable */
    import ListImageComponent from "./ListImageComponent";
    import Dialog from "./Dialog";

    export default {
        name: "Description",
        components: {Dialog, ListImageComponent},
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
                dialog: false,
                overlay: false,

            }
        },
        methods: {
            changeImage(image) {
                this.currentImage = image
            },
            toggleModal() {
                if (this.isSubscribed) {
                    this.isSubscribed = false
                } else {
                    this.dialog = !this.dialog;
                }

            },
            subscribeUser() {
                this.toggleModal();
                this.overlay = true;
                setTimeout(() => {
                    console.log(this.overlay);
                    this.overlay = false;
                    this.isSubscribed = true;

                }, 4000);

            },

        },
    }
</script>

<style scoped>
    .productInfo {
        background: #ECEFF1
    }
    .headers {
        font-size: 2.5vw;
        text-align: center;
        font-weight: bold;
        margin-bottom: 0;
    }

    p {
        font-size: 0.9vw;
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