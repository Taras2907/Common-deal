<template>
  <v-card color="basil">
    <v-card-title class="text-center justify-center py-6">
      <h3 class="font-weight-bold basil--text">{{ this.product.name }}</h3>
    </v-card-title>

    <v-tabs
      v-model="tab"
      background-color="transparent"
      color="basil"
      grow
      show-arrows
    >
      <v-tab v-for="item in items" :key="item.id">
        {{ item.name }}
      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab" class="image">
      <v-tab-item :key="1">
        <v-card color="basil" flat>
          <Description
            :product="product"
            :shortDescription="shortDescription"
            :expirationDate="expirationDate"
            :image="currentImage"
            @change-image="changeImage"
            @toggle-overlay="toggleOverlay"
          ></Description>
        </v-card>
      </v-tab-item>
      <v-tab-item :key="2">
        <v-card color="basil" flat>
          <v-row
            class="mx-0 px-0"
            v-for="(value, key) in product.attributes"
            :key="key"
          >
            <v-col class="px-0" col="4">
              <span class="pl-5">{{ key }}</span>
            </v-col>

            <v-col class="px-0" col="8">
              <span>{{ value }}</span>
            </v-col>
          </v-row>
        </v-card>
      </v-tab-item>

      <v-tab-item :key="3">
        <Reviews></Reviews>
      </v-tab-item>

      <v-tab-item :key="4">
        <Shipping></Shipping>
      </v-tab-item>
    </v-tabs-items>
    <div class="text-center">
      <v-overlay :value="overlay">
        <v-progress-circular indeterminate color="amber"></v-progress-circular>
      </v-overlay>
    </div>
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
                currentImage: "",
                overlay: false,
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
                        this.currentImage = json_response.image;
                        this.setTimer(this.product.expiration_date);
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
            },
            changeImage(image) {
                console.log(image);
                this.currentImage = image;
            },
            toggleOverlay() {
                this.overlay = !this.overlay
            }
        },
        created() {
            this.getProductData()
        }
    }
</script>

<style scoped>
</style>