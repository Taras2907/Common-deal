<template>
    <v-container fluid>
        <v-list>
            <v-list-item-group v-model="item" color="primary">
                <v-list-item
                        v-for="(item, i) in items"
                        :key="i"
                >
                    <v-list-item-content>
                        <v-card flat tile class="d-flex">
                            <v-img contain
                                   class="grey lighten-2"
                                   aspect-ratio="1"
                                   @click="triggerChangeMainImage(item)"
                                   :lazy-src="`https://frontendcommondeal.blob.core.windows.net/%24web/img/${item}`"
                                   :src="`https://frontendcommondeal.blob.core.windows.net/%24web/img/${item}`"></v-img>
                        </v-card>

                    </v-list-item-content>
                </v-list-item>
            </v-list-item-group>
        </v-list>
    </v-container>
</template>

<script>
    export default {
        name: "ListImageComponent",
        data() {
            return {
                items: [
                    "asus1.jpeg",
                    "asus2.jpeg",
                    "asus3.jpg",
                    "asus4.jpg",
                ],
                item: null,
                isSelected: null,
            }
        },
        methods: {
            triggerChangeMainImage(image) {
                this.$emit('change-image', image);
            }
        }
    }
</script>

<style scoped>

</style>