<template>
    <div
            class="container tab-pane fade show active"
            id="login"
            role="tabpanel"
            aria-labelledby="pills-home-tab"
    >
        <div class="form-group">

            <div class="text-left pl-2">
                <label for="loginUserEmail">Enter Username</label>
            </div>

            <input
                    name="userEmail"
                    type="text"
                    class="form-control"
                    id="loginUserEmail"
                    aria-describedby="loginHelp"
                    placeholder="Username"
                    required
            />
            <small id="loginHelp" class="form-text text-muted"
            >Enter your login and password and press submit
            </small>
        </div>
        <div class="form-group">
            <div class="row-no-gutters px-0 mx-0 text-left">
                <label class="col-sm-6 text-left pl-2" for="loginPassword">Password</label>
                <router-link class="col-sm-6 text-left pl-2"
                             :to="{name: 'password-recover'}"
                >Forgot password?</router-link>
            </div>

            <input
                    name="password"
                    type="password"
                    class="form-control"
                    id="loginPassword"
                    placeholder="Password"
                    required
            />
        </div>
        <button type="button" class="btn btn-primary" id="loginSubmit">
            Submit
        </button>
    </div>
</template>

<script>
    /* eslint-disable */
    export default {
        name: "LoginComponent"
    }
</script>

<style scoped>

</style>