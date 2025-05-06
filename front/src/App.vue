<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router"; // 📌 Importamos Vue Router

</script>

<template>
  <v-app>
    <v-app-bar color="primary" dark>
      <v-toolbar-title>HR-Core</v-toolbar-title>
      <v-spacer />
      <v-btn text to="/empleados">Empleados</v-btn>
      <v-btn text to="/contratos">Contratos</v-btn>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>


