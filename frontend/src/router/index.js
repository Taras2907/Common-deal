import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import NotFound from "../views/NotFound.vue";
import Authenticaction from "../views/Authentication.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: Home
  },
  {
    path: "/authentication",
    name: "authentication",
    component: Authenticaction
  },
  {
    path: "*",
    name: "page-not-found",
    component: NotFound
  }
];

const router = new VueRouter({
  mode: "history",
  base: null,
  routes
});

export default router;
