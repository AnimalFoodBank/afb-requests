<script setup lang="ts">
import { HomeIcon } from '@heroicons/vue/24/solid';
import axios from 'axios';
import router from '../router';
import { useAuthStore } from '../stores/auth';
const authStore = useAuthStore();

const handleSubmit = (form$: any) => {
  console.log('LoginView.handleSubmit()')

  axios.post('/auth-token/', form$.requestData, {
    headers: {},
    withCredentials: true,
  })
    .then(response => {
      console.log(response);
      const token = response.data.token;
      authStore.login(token);
      router.push("/dashboard");  // TODO: Get route from router
    })
    .catch(error => {
      // TODO: Handle login failure
      console.log(error);
    });

}


</script>

<template>
  <div class="flex min-h-full flex-1">
    <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
      <div class="mx-auto w-full max-w-sm lg:w-96">
        <div>
          <router-link :to="{ name: 'HomePageView' }">
            <HomeIcon class="h-10 w-full" />
          </router-link>
          <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
          <p class="mt-2 text-sm leading-6 text-gray-500">
            Not a member?
            &nbsp;
            <router-link :to="{ name: 'RegisterView' }" class="font-semibold text-indigo-600 hover:text-indigo-500">
              Register </router-link>
          </p>
        </div>

        <div class="mt-10">
          <!-- Validate only on submit -->
          <!-- See the API reference docs for VueForm -->
          <!-- https://vueform.com/reference/vueform#option-endpoint -->
          <Vueform :display-errors="false" ref="form$" :endpoint="false">
            <TextElement name="username" input-type="text" label="Email address" placeholder=""
                         :rules="['required', 'email']" :debounce="100" />
            <TextElement name="password" input-type="password" label="Password" />
            <ButtonElement name="button" @click="handleSubmit">
              Login
            </ButtonElement>
          </Vueform>
        </div>

      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block">
      <img class="h-800" alt="Become an AFB membver today" src='@/assets/img/Dog-Sideways-Glare-1024x1024.png'>
    </div>
  </div>
</template>

<style scoped>
</style>

<!--

/*
* Validation rules can asynchronous. For example
* unique rules sends a request to and endpoint and
* waits for the answer before deciding if the
* element's value is valid:
*
*     <TextElement rules="nullable|unique:users" />
*
* Endpoints can be configured in vueform.config.js.
* See configuration options at unique and exists
* rules.
*
* @see https://vueform.com/docs/validating-elements#asnyc-rules
*/

 -->
