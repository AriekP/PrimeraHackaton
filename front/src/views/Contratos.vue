<template>
    <v-container class="py-4">
      <h2>Gestión de Contratos</h2>
      <contrato-form @guardado="listar" />
      <contrato-list :items="contratos" />
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import { fetchContratos } from "../services/api";
  import ContratoForm from "../components/ContratoForm.vue";
  import ContratoList from "../components/ContratoList.vue";
  
  const contratos = ref([]);
  
  const listar = async () => {
    const res = await fetchContratos();
    contratos.value = res.data;
  };
  
  onMounted(listar);
  </script>
  