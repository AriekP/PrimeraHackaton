import { createRouter, createWebHistory } from "vue-router";
import Empleados from "../views/Empleados.vue";
import Contratos from "../views/Contratos.vue";

const routes = [
  { path: "/", redirect: "/empleados" },
  { path: "/empleados", component: Empleados },
  { path: "/contratos",  component: Contratos },
];

export default createRouter({
  history: createWebHistory(),
  routes,
});
