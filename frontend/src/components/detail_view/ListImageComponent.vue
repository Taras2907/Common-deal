<template>
    <v-list>
        <v-list-item-group v-model="item" color="primary">
            <v-list-item class="px-1 py-0"
                    v-for="(item, i) in items"
                    :key="i"
            >
                <v-list-item-content class="py-1">
                    <v-img contain
                           aspect-ratio="1"
                           @click="triggerChangeMainImage(item)"
                           :lazy-src="`https://frontendcommondeal.blob.core.windows.net/%24web/img/${item}`"
                           :src="`https://frontendcommondeal.blob.core.windows.net/%24web/img/${item}`"></v-img>

                </v-list-item-content>
            </v-list-item>
        </v-list-item-group>
    </v-list>
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