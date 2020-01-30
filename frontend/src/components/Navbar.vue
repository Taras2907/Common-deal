<template>
    <div class="container-fluid px-0 mt-0 pt-0">
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01"
                    aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
                <a class="navbar-brand" href="#">Common Deal</a>
                <ul class="navbar-nav mr-4 mt-2 mt-lg-0">
                    <li class="nav-item active">
                        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link disabled" href="#">Disabled</a>
                    </li>
                </ul>
                <div class="container-fluid">
                    <AutoSuggest class="mr-auto"/>
                </div>
                <div class="container-fluid w-25">
                    <button class="btn-outline-primary"><i class="fa" style="font-size:24px">&#xf07a;</i></button>
                    <span class='badge badge-warning ' id='lblCartCount'>  1</span>
                    <button class="btn-outline-primary">Sign up</button>
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