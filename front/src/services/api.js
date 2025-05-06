import axios from "axios";

export const api = axios.create({
  baseURL: "http://localhost:8002", // tu HR-Core
  headers: { "Content-Type": "application/json" }
});

// Empleados
export const fetchEmpleados = (params) =>
  api.get("/empleados/", { params });
export const createEmpleado = (data) =>
  api.post("/empleados/", data);
export const updateEmpleado = (id, data) =>
  api.put(`/empleados/${id}`, data);
export const deleteEmpleado = (id) =>
  api.delete(`/empleados/${id}`);

// Contratos
export const fetchContratos = (params) =>
  api.get("/contratos/", { params });
export const createContrato = (data) =>
  api.post("/contratos/", data);
