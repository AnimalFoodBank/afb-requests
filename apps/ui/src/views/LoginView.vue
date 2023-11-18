<script setup lang="ts">
import { HomeIcon } from '@heroicons/vue/24/solid';

// const handleSubmit = (form$: any) => {
//   console.log('LoginView.handleSubmit()')
//   console.log(form$);

//   // TODO: Add validation logic here
//   const response_via_submit = form$.submit();
//   console.log(response_via_submit.data);

//   // const response = axios.post('/api/auth/login/', form$.values())
//   // console.log(response);
// }


// async function prepareForm(data: any) {
//   try {
//     await console.log('LoginView.prepareForm()')
//     console.log(data);
//   } catch (error) {
//     throw error // this will cancel the submit process
//   }
// }

// async function getCsrfToken() {
//   axios.get("sanctum/csrf-cookie");
// }

// async function login(email: string, password: string) {
//   const response = await axios.post('/login', { email, password });
//   const token = response.data.token;

//   // Save the token in local storage or in a cookie
//   localStorage.setItem('token', token);
// }

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

</script>

<template>
  <!--
    This example requires updating your template:

    ```
    <html class="h-full bg-gray-50">
    <body class="h-full">
      ```
    -->

    <div class="flex min-h-full flex-1">
      <div class="flex flex-1 flex-col justify-center px-4 py-12 sm:px-6 lg:flex-none lg:px-20 xl:px-24">
        <div class="mx-auto w-full max-w-sm lg:w-96">
          <div>
            <router-link :to="{ name: 'DashboardView' }"> <HomeIcon class="h-10 w-full" /> </router-link>
            <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
            <p class="mt-2 text-sm leading-6 text-gray-500">
              Not a member?
              &nbsp;
              <router-link :to="{ name: 'RegisterView' }" class="font-semibold text-indigo-600 hover:text-indigo-500"> Register </router-link>
            </p>
          </div>

          <div class="mt-10">

            <!-- Validate only on submit -->
            <Vueform
            :display-errors="false" ref="form$"
            endpoint="/api/auth/login/"
            method="POST"
            >
            <TextElement name="email" input-type="text" label="Email address" placeholder="" :rules="['required', 'email']" :debounce="100" />
            <TextElement name="password" input-type="password" label="Password" />
            <ButtonElement name="button" submits>
              Login
            </ButtonElement>
          </Vueform>
        </div>

      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block">
      <!-- <CatHeartImage class="absolute inset-0 h-full w-full object-cover" /> -->
      <img alt="Become an AFB membver today" src='@/assets/img/Cat-Heart-680x800-1.png'>
    </div>
  </div>
</template>

<style scoped>
</style>
