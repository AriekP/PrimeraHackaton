<template>
    <v-card class="mb-4 pa-4">
      <v-form @submit.prevent="submit">
        <v-row>
          <v-col cols="12" md="4">
            <v-text-field
              v-model.number="form.empleado_id"
              label="ID Empleado"
              type="number"
              required
            />
          </v-col>
          <v-col cols="12" md="4">
            <!-- CAMBIO: input de fecha nativo -->
            <v-text-field
              v-model="form.fecha_inicio"
              label="Fecha Inicio"
              type="date"
              required
            />
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              v-model.number="form.salario"
              label="Salario"
              type="number"
              required
            />
          </v-col>
          <v-col cols="12" md="4">
            <v-text-field
              v-model.number="form.periodo_prueba"
              label="Días de Prueba"
              type="number"
              required
            />
          </v-col>
          <v-col cols="12" md="8">
            <v-text-field
              v-model="form.ruta_plantilla"
              label="Ruta Plantilla (opcional)"
            />
          </v-col>
          <v-col cols="12" class="d-flex justify-end">
            <v-btn type="submit" color="primary">Guardar Contrato</v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-card>
  </template>
  
  <script setup>
  import { reactive } from "vue";
  import { createContrato } from "../services/api";
  
  const emit = defineEmits(["guardado"]);
  const form = reactive({
    empleado_id: null,
    fecha_inicio: "",
    salario: null,
    periodo_prueba: null,
    ruta_plantilla: ""
  });
  
  const submit = async () => {
    await createContrato(form);
    Object.keys(form).forEach(k => (form[k] = k === "ruta_plantilla" ? "" : null));
    emit("guardado");
  };
  </script>
  