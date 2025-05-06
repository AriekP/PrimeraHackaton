<template>
    <v-card class="mb-4 pa-4">
      <v-form @submit.prevent="submit">
        <v-row>
          <!-- oculto, pero importante para update -->
          <input type="hidden" v-model="form.id" />
  
          <!-- Campos visibles -->
          <v-col cols="12" md="6">
            <v-text-field v-model="form.nombre" label="Nombre" required />
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field v-model="form.apellido" label="Apellido" required />
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field v-model="form.area" label="Área" required />
          </v-col>
          <v-col cols="12" md="6">
            <v-text-field v-model="form.cargo" label="Cargo" required />
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
              v-model="form.fecha_ingreso"
              label="Fecha Ingreso"
              type="date"
              required
            />
          </v-col>
          <!-- Ejemplo de campo extra -->
          <v-col cols="12" md="4">
            <v-checkbox
              v-model="form.activo"
              label="Activo"
            />
          </v-col>
  
          <!-- Botones -->
          <v-col cols="12" class="d-flex justify-end">
            <v-btn text @click="$emit('cancel')">Cancelar</v-btn>
            <v-btn type="submit" color="primary">
              {{ edicion ? "Actualizar" : "Crear" }}
            </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </v-card>
  </template>
  
  <script setup>
  import { reactive, watch } from "vue";
  import { createEmpleado, updateEmpleado } from "../services/api";
  
  const props = defineProps({
    edicion: { type: Boolean, default: false },
    initial: { type: Object, default: null },
  });
  const emit = defineEmits(["guardado", "cancel"]);
  
  // 1) Incluye *todos* los campos que quieras manejar
  const form = reactive({
    id: null,
    nombre: "",
    apellido: "",
    area: "",
    cargo: "",
    salario: null,
    fecha_ingreso: "",
    activo: true,       // ejemplo de campo extra
    // ... más si los necesitas
  });
  
  // 2) Cuando `initial` cambie, recarga el form
  watch(
    () => props.initial,
    (emp) => {
      if (emp) {
        Object.assign(form, emp);
      } else {
        // reset a valores por defecto
        form.id = null;
        form.nombre = "";
        form.apellido = "";
        form.area = "";
        form.cargo = "";
        form.salario = null;
        form.fecha_ingreso = "";
        form.activo = true;
      }
    },
    { immediate: true }
  );
  
  // 3) Al enviar, elige create u update
  const submit = async () => {
    const payload = {
      nombre: form.nombre,
      apellido: form.apellido,
      area: form.area,
      cargo: form.cargo,
      salario: form.salario,
      fecha_ingreso: form.fecha_ingreso,
      activo: form.activo,
      // …incluye lo que necesites
    };
    if (props.edicion && form.id) {
      await updateEmpleado(form.id, payload);
    } else {
      await createEmpleado(payload);
    }
    emit("guardado");
  };
  </script>
  