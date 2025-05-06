<template>
    <v-container class="py-4">
      <h2>Gestión de Empleados</h2>
  
      <!-- Formulario de alta/edición -->
      <empleado-form
        :edicion="editando"
        :initial="empleadoSeleccionado"
        @guardado="onGuardado"
        @cancel="cancelarEdicion"
      />
  
      <!-- Tabla con buscador, editar y eliminar -->
      <empleado-list
        :items="empleados"
        @eliminar="eliminar"
        @editar="iniciarEdicion"
      />
    </v-container>
  </template>
  
  <script setup>
  import { ref, onMounted } from "vue";
  import {
    fetchEmpleados,
    deleteEmpleado,
  } from "../services/api";
  import EmpleadoForm from "../components/EmpleadoForm.vue";
  import EmpleadoList from "../components/EmpleadoList.vue";
  
  const empleados = ref([]);
  const editando = ref(false);
  const empleadoSeleccionado = ref(null);
  
  const listar = async () => {
    const res = await fetchEmpleados();
    empleados.value = res.data;
  };
  
  const eliminar = async (id) => {
    await deleteEmpleado(id);
    await listar();
  };
  
  const iniciarEdicion = (empleado) => {
    empleadoSeleccionado.value = { ...empleado };
    editando.value = true;
  };
  
  const cancelarEdicion = () => {
    editando.value = false;
    empleadoSeleccionado.value = null;
  };
  
  const onGuardado = async () => {
    editando.value = false;
    empleadoSeleccionado.value = null;
    await listar();
  };
  
  onMounted(listar);
  </script>
  