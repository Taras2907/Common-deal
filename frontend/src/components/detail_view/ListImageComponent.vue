<template>
    <v-container fluid>
        <v-list>
            <v-list-item-group v-model="item" color="primary">
                <v-list-item
                        v-for="(item, i) in items"
                        :key="i"
                >
                    <v-list-item-content>
                        <v-img max-height="150"
                               max-width="150"

                               @click="triggerChangeMainImage(item)"
                               :src="item"></v-img>
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
                    "https://i1.rozetka.ua/goods/13680232/copy_asus_90nr01l3_m02600_5d67deff8ce7c_images_13680232057.jpg",
                    "https://i1.rozetka.ua/goods/13680234/copy_asus_90nr01l3_m02600_5d67deff8ce7c_images_13680234793.jpg",
                    "https://i2.rozetka.ua/goods/13680377/asus_90nr01l3_m02610_images_13680377623.jpg",
                ],
                item: null,
                isSelected: null,
            }
        },
        methods:{
            triggerChangeMainImage(image){
                this.$emit('change-image', image);
            }
        }
    }
</script>

<style scoped>

</style>