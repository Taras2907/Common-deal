<template>
    <v-card>

        <v-card-title>
            Komputr
        </v-card-title>

        <v-img
        src="https://pngimg.com/uploads/computer_pc/computer_pc_PNG7713.png"
        contain
        class="ma-2"
        fluid></v-img>

        <v-card-text>
            Very big komputr
        </v-card-text>

        <v-container>
            <v-row no-gutters>
                <v-col cols="8" >
                    <v-progress-linear
                        height="20"
                        value="88"
                        stream
                        color="#FFA000">
                        <strong>88%</strong>
                    </v-progress-linear></v-col>
                <v-col cols="4" align="center"><strong>1234,00 </strong>zł</v-col>
            </v-row>
        </v-container>

    </v-card>
</template>

<script>
    export default {
        name: "Product"
    }
</script>

<style scoped>

</style>