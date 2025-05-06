<template>
    <v-data-table
      :items="items"
      :headers="headers"
      class="elevation-1"
    />
  </template>
  
  <script setup>
  const props = defineProps({
    items: { type: Array, default: () => [] }
  });
  
  const headers = [
    { title: "ID", key: "id" },
    { title: "Empleado ID", key: "empleado_id" },
    { title: "Inicio", key: "fecha_inicio" },
    { title: "Salario", key: "salario" },
    { title: "Prueba (días)", key: "periodo_prueba" },
    { title: "Plantilla", key: "ruta_plantilla" },
    { title: "Creado", key: "fecha_creado" }
  ];
  </script>
  