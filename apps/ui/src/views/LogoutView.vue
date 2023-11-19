<script setup lang="ts">
import axios from 'axios';
import { onMounted } from 'vue';
import router from '../router';
import { useAuthStore } from '../stores/auth';
const authStore = useAuthStore();
// Create an instance of axios to use in this module.
// See defaults set in /src/main.ts
const http_client = axios.create();

// Set the AUTH token for any request
http_client.interceptors.request.use(function (config) {
  if (authStore.isAuthenticated) {
    const token = authStore.getToken;
    console.log('http_client.interceptors.request.use()', token);
    config.headers.Authorization = token ? `Token ${token}` : '';
  }
  return config;
});


onMounted(async () => {

  console.log('LogoutView.onMounted()')

  axios.delete('/users/expire_token/')
    .then(response => {
      console.log(response);
      authStore.logout();
      router.push("/");
    })
    .catch(error => {
      // TODO: Handle login failure
      console.log(error);
      router.push("/");
    });
});


</script>

<template>

</template>
