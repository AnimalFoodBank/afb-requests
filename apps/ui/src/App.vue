
<!-- https://vuejs.org/guide/essentials/component-basics.html#dynamic-components -->
<template>
  <component :is="$route.meta.layout || 'div'">
    <router-view />
  </component>
</template>

<script setup lang="ts">
import CatHeartImage from '@/assets/img/Cat-Heart-680x800-1.png';
import { onMounted, ref } from 'vue';

// Demonstrates how to use environment variables in Vue components.
console.log('import.meta.env.VITE_BASE_URL=' + import.meta.env.VITE_BASE_URL)

const user = ref({
  isLoggedIn: false,
  name: '',
  email: '',
  imageUrl: '',
});

/**
* Makes a GET request to the current user endpoint and sets the user value if the response status is within the 200-299 range.
* If the response status is outside the 200-299 range, an error message is logged to the console.
* If there is a network error or the request is rejected, an error message is logged to the console.
* Note: axios automatically rejects the promise if the status code is outside the 200-299 range, so the else branch in this example might not be necessary depending on your axios configuration.
*/
onMounted(async () => {
  // try {
  //   const response = await axios.get('/api/users/current_user/');
  //   if (response.status >= 200 && response.status < 300) {
  //     user.value = response.data;
  //   } else {
  //     console.error(`Request failed with status code ${response.status}`);
  //     user.value = guestUser.value;
  //   }
  // } catch (error) {
  //   console.error('Request failed', error);
  //   user.value = guestUser.value;
  // }
});

const guestUser = ref({
  isLoggedIn: false,
  name: 'Heart Cat',
  email: 'heartcat@animalfoodbank.org',
  imageUrl: CatHeartImage,
});
</script>



<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
