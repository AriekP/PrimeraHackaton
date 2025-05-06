<template>
    <div>
      <!-- Buscador con debounce -->
      <v-text-field
        v-model="search"
        label="Buscar empleados..."
        append-icon="mdi-magnify"
        class="mb-4"
        clearable
        :loading="loading"
        @update:modelValue="handleSearch"
      />
  
      <!-- Estado de carga -->
      <v-progress-linear
        v-if="loading"
        indeterminate
        color="primary"
        class="mb-2"
      />
  
      <!-- Tabla con sorting y estilo mejorado -->
      <v-data-table
        :headers="headers"
        :items="filtered"
        :sort-by="sortBy"
        :sort-desc="sortDesc"
        class="elevation-1"
        :loading="loading"
        loading-text="Cargando empleados..."
        :items-per-page="10"
        :footer-props="{
          'items-per-page-options': [10, 20, 50]
        }"
      >
        <!-- Formato salario -->
        <template #item.salario="{ value }">
          {{ formatCurrency(value) }}
        </template>
  
        <!-- Acciones con a11y -->
        <template #item.actions="{ item }">
    <div class="d-flex align-center justify-end">
      <v-btn
        small
        color="primary"
        class="mr-2"
        @click="$emit('editar', item)"
        aria-label="Modificar empleado"
      >
        Modificar
      </v-btn>
      
      <v-btn
        small
        color="error"
        @click="openDeleteDialog(item)"
        aria-label="Eliminar empleado"
      >
        Eliminar
      </v-btn>
    </div>
  </template>
  
        <!-- Estado vacío -->
        <template #no-data>
          <v-alert
            type="info"
            class="ma-4"
          >
            No se encontraron empleados
          </v-alert>
        </template>
      </v-data-table>
  
      <!-- Dialogo de confirmación -->
      <v-dialog
        v-model="deleteDialog"
        max-width="400"
      >
        <v-card>
          <v-card-title class="text-h6">
            Confirmar eliminación
          </v-card-title>
          <v-card-text>
            ¿Estás seguro de querer eliminar este empleado?
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="secondary"
              @click="deleteDialog = false"
            >
              Cancelar
            </v-btn>
            <v-btn
              color="error"
              @click="confirmDelete"
            >
              Eliminar
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
  </template>
  
  <script setup>
  import { ref, computed, watch } from 'vue'
  import { debounce } from 'lodash'
  
  const props = defineProps({
    items: { type: Array, default: () => [] },
    loading: { type: Boolean, default: false }
  })
  
  const emit = defineEmits(['eliminar', 'editar', 'search'])
  
  const headers = [
    { text: 'Nombre', value: 'nombre', sortable: true },
    { text: 'Apellido', value: 'apellido', sortable: true },
    { text: 'Área', value: 'area', sortable: true },
    { text: 'Cargo', value: 'cargo', sortable: true },
    { text: 'Salario', value: 'salario', sortable: true },
    { text: 'Acciones', value: 'actions', sortable: false }
  ]
  
  const search = ref('')
  const sortBy = ref(['nombre'])
  const sortDesc = ref([false])
  const deleteDialog = ref(false)
  const selectedItem = ref(null)
  
  // Mejor filtrado con debounce
  const handleSearch = debounce(value => {
    emit('search', value) // Para posible filtrado server-side
  }, 300)
  
  // Formateo de moneda
  const formatCurrency = value => {
    return new Intl.NumberFormat('es-ES', {
      style: 'currency',
      currency: 'EUR'
    }).format(value)
  }
  
  // Filtrado cliente-side mejorado
  const filtered = computed(() => {
    const term = search.value?.toLowerCase() || ''
    return props.items.filter(item => {
      const searchString = Object.values(item)
        .join(' ')
        .toLowerCase()
      return searchString.includes(term)
    })
  })
  
  // Eliminación con diálogo
  const openDeleteDialog = item => {
    selectedItem.value = item
    deleteDialog.value = true
  }
  
  const confirmDelete = () => {
    emit('eliminar', selectedItem.value.id)
    deleteDialog.value = false
  }
  </script>
  
  <style scoped>
  .v-data-table >>> tbody tr:hover {
    background-color: rgba(0, 0, 0, 0.04);
  }
  </style>