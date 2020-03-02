<template>
  <v-card>
    <v-card-title>
      {{ product.name }}
    </v-card-title>

    <v-img
      :src="product.image"
      contain
      class="ma-2"
      aspect-ratio="1.5"
      fluid
    ></v-img>

    <v-container>
      <v-row no-gutters>
        <v-col cols="8">
          <v-progress-linear height="20" value="88" stream color="#FFA000">
            <strong>88%</strong>
          </v-progress-linear></v-col
        >
        <v-col cols="4" align="center"
          ><strong>{{ product.price }} </strong>zł</v-col
        >
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: "Product",
  props: {
    product: {
      type: Object,
      required: true
    }
  }
};
</script>

<style scoped></style>
