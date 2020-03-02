<template>
  <v-navigation-drawer v-model="drawer" app color="#ECEFF1" clipped>
    <v-list>
      <v-list-group
        v-for="category in productCategories"
        :key="category.name"
        v-model="category.active"
        no-action
      >
        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="category.name"></v-list-item-title>
          </v-list-item-content>
        </template>

        <v-list-item
          v-for="subcategory in category.subcategories"
          :key="subcategory.name"
          @click="
            $router.push({
              name: 'category',
              params: { category: subcategory.name.toLowerCase() }
            })
          "
        >
          <v-list-item-content>
            <v-list-item-title v-text="subcategory.name"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-group>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
import { apiService } from "../../common/apiService";

export default {
  name: "Drawer",
  data() {
    return {
      productCategories: [],
      drawer: null
    };
  },
  mounted() {
    this.$root.$on("toggleDrawer", () => {
      this.drawer = !this.drawer;
    });
  },
  methods: {
    getProductCategories() {
      let endpoint = `/api/product-categories/`;
      apiService(endpoint, "GET")
        .then(response => response.json())
        .then(json_response => {
          this.productCategories = json_response;
        });
    }
  },
  created() {
    this.getProductCategories();
  }
};
</script>

<style scoped></style>
