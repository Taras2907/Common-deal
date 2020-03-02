<template>
  <v-list>
    <v-list-item-group v-model="image" color="primary">
      <v-list-item class="px-1 py-0" v-for="(image, i) in images" :key="i">
        <v-list-item-content class="py-1">
          <v-img
            contain
            aspect-ratio="1"
            @click="triggerChangeMainImage(image.image)"
            :lazy-src="image.image"
            :src="image.image"
          ></v-img>
        </v-list-item-content>
      </v-list-item>
    </v-list-item-group>
  </v-list>
</template>

<script>
export default {
  name: "ListImageComponent",
  props: ["images"],
  data() {
    return {
      image: null,
      isSelected: null
    };
  },
  methods: {
    triggerChangeMainImage(image) {
      this.$emit("change-image", image);
    }
  }
};
</script>

<style scoped></style>
