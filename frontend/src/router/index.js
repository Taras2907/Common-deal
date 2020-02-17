import Vue from "vue";
import VueRouter from "vue-router";
// import Home from "../views/Home.vue";
import NotFound from "../views/NotFound.vue";
import DetailView from "../views/DetailView.vue"
import Authenticaction from "../views/Authentication.vue";
import PasswordRecover from "../views/PasswordRecover.vue";
import PasswordRecoverConfirm from "../views/PasswordRecoverConfirm.vue";
import Index from "../views/Index";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "home",
        component: Index
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
    },
    {
        path: "/password/recover",
        name: "password-recover",
        component: PasswordRecover
    },
    {
        path: "/password/confirm/:uid/:token",
        name: "password-recover-confirm",
        component: PasswordRecoverConfirm,
        props: true
    },
    {
        path: "/products/:id",
        name: "product-detail",
        component: DetailView,
        props: true
    }
];

const router = new VueRouter({
    mode: "history",
    base: null,
    routes
});

export default router;
