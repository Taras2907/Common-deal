<template>
    <v-menu offset-y bottom>
        <template v-slot:activator="{ on }">
            <v-btn
                    v-on="on"
            >{{username}}
                <v-icon>mdi-dots-vertical</v-icon>
            </v-btn>
        </template>

        <v-list>
            <!--      <v-list-item>-->
            <!--        <v-list-item-title>1</v-list-item-title>-->
            <!--      </v-list-item>-->
            <!--      <v-list-item>-->
            <!--        <v-list-item-title>2</v-list-item-title>-->
            <!--      </v-list-item>-->
            <v-divider></v-divider>
            <v-list-item>
                <v-list-item-title @click="logoutUser"><a>Sign out</a></v-list-item-title>
            </v-list-item>
        </v-list>
    </v-menu>
</template>

<script>
    import {apiService} from "../../common/apiService";

    export default {
        name: "Menu",
        data() {
            return {
                username: localStorage.username,

            }
        },
        methods: {
            logoutUser() {
                let endpoint = `/api/rest-auth/logout/`;
                apiService(endpoint, 'POST')
                    .then(response => response.json())
                    .then(responseData => {
                        if (responseData.ok) {
                            this.$root.$emit('logout-user');
                            this.username = null;
                            localStorage.removeItem("username");
                            this.$router.push("/");
                        }


                    })
                    .catch(error => console.log(error))
            }
        }
    }
</script>

<style scoped>

</style>