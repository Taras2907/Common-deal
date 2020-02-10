<template>
    <div class="container-fluid px-0 mt-0 pt-0">
        <nav class="navbar navbar-expand-lg navbar-light bg-secondary">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01"
                    aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
                <router-link class="navbar-brand" :to="{name:'home'}">Common Deal</router-link>
                <ul class="navbar-nav mr-4 mt-2 mt-lg-0">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">About<span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" href="#">Disabled</a>
                    </li>
                </ul>
                <div class="container-fluid">
                    <AutoSuggest/>
                </div>
                <div class="container-fluid w-25 ml-auto">
                    <button class="btn-primary mx-1">Cart</button>
                    <button class="btn-primary mx-1" @click="redirectToLoginView">Sign Up</button>

                </div>

            </div>
        </nav>
    </div>


</template>

<script>
    /* eslint-disable */

    import AutoSuggest from "./AutoSuggest";

    export default {
        name: "Navbar",
        components: {AutoSuggest},
        methods:{
            redirectToLoginView(){
                this.$router.push("/authentication")
            }
        }
    }
</script>

<style scoped>
    .nav-link {
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }

    .badge {
        padding-left: 9px;
        padding-right: 9px;
        -webkit-border-radius: 9px;
        -moz-border-radius: 9px;
        border-radius: 9px;
    }

    .label-warning[href],
    .badge-warning[href] {
        background-color: #c67605;
    }

    #lblCartCount {
        font-size: 12px;
        background: #ff0000;
        color: #fff;
        padding: 0 5px;
        vertical-align: top;
        margin-left: -10px;
    }

</style>