<script setup>
import { ref } from "vue";
import axios from "axios";
import { useRouter } from "vue-router";

const email = ref("");
const password = ref("");
const errorMessage = ref("");  // 🔹 Mensaje de error visible para el usuario
const router = useRouter();

const login = async () => {
    try {
        const response = await axios.post("http://127.0.0.1:5002/usuarios/login/", {
            username: email.value,
            password: password.value,
        }, {
            headers: { "Content-Type": "application/x-www-form-urlencoded" }
        });

        localStorage.setItem("token", response.data.access_token);
        alert("Inicio de sesión exitoso ✅");
        errorMessage.value = "";  // 🔹 Limpiar el mensaje de error si el login es exitoso
        router.push("/dashboard");  
    } catch (error) {
        console.error("Error al iniciar sesión:", error);
        
        if (error.response && error.response.status === 401) {
            errorMessage.value = "❌ Credenciales incorrectas. Intenta de nuevo.";
        } else {
            errorMessage.value = "⚠ Ocurrió un error al conectar con el servidor.";
        }
    }
};
</script>

<template>
    <v-app>
        <v-container>
            <v-card class="pa-5">
                <h1 class="text-h5">Login</h1>
                <v-form @submit.prevent="login">
                    <v-text-field v-model="email" label="Email" type="email" required></v-text-field>
                    <v-text-field v-model="password" label="Contraseña" type="password" required></v-text-field>
                    <v-btn type="submit" color="primary">Iniciar Sesión</v-btn>
                </v-form>
                <p v-if="errorMessage" class="text-red">{{ errorMessage }}</p>
            </v-card>
        </v-container>
    </v-app>
</template>
