<template>
  <div
    class="container tab-pane fade show active"
    id="login"
    role="tabpanel"
    aria-labelledby="pills-home-tab"
  >
    <div class="form-group">
      <label for="loginUserEmail">Enter Username</label>
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
        >Enter your login and password and press submit button
      </small>
    </div>
    <div class="form-group">
      <label for="loginPassword">Password</label>
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