<template>
    <v-card tile class="d-flex mx-auto" max-width="600px" max-height="700px">
        <v-tabs centered v-model="tab" fixed-tabs>

            <v-tab :key="1">Login</v-tab>
            <v-tab :key="2">Registration</v-tab>

            <v-tab-item :key="1">
                <LoginComponent></LoginComponent>
            </v-tab-item>

            <v-tab-item :key="2">
                <RegistrationComponent></RegistrationComponent>
            </v-tab-item>
        </v-tabs>
    </v-card>

</template>

<script>
    /* eslint-disable */
    import RegistrationComponent from "@/components/Registration";
    import LoginComponent from "../components/Login";

    export default {
        name: "Authentication",
        components: {LoginComponent, RegistrationComponent},
        data() {
            return {
                tab: null,
            }
        },
        methods: {
        }
    }
</script>

<style scoped>
</style>