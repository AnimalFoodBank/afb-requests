<!--
  This example requires some changes to your config:

  ```
  // tailwind.config.js
  module.exports = {
    // ...
    plugins: [
    // ...
    require('@tailwindcss/forms'),
    ],
  }
  ```
-->
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
            <router-link :to="{ name: 'DashboardView' }">
              <HomeIcon class="h-10 w-full" />
            </router-link>
            <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Client Registration</h2>
            <p class="mt-2 text-sm leading-6 text-gray-500">
              Already registered?
              &nbsp;
              <router-link :to="{ name: 'LoginView' }" class="font-semibold text-indigo-600 hover:text-indigo-500"> Login
              </router-link>
            </p>
          </div>

          <div class="mt-10">


            <Vueform>
              <template #empty>
                <FormSteps>
                  <FormStep name="account" :elements="['email', 'password']">Account</FormStep>
                  <FormStep name="personal" :elements="['name', 'bio']">Personal</FormStep>
                  <FormStep name="social" :elements="['facebook', 'twitter']">Social</FormStep>
                </FormSteps>

                <FormElements>
                  <TextElement name="email" label="Email" />
                  <TextElement input-type="password" name="password" label="Password" />
                  <TextElement name="name" label="Name" />
                  <TextareaElement name="bio" label="bio" />
                  <TextElement name="facebook" label="Facebook" />
                  <TextElement name="twitter" label="Twitter" />
                </FormElements>

                <FormStepsControls />
              </template>
            </Vueform>

          </div>

        </div>
      </div>
      <div class="relative hidden w-0 flex-1 lg:block">
        <!-- <CatHeartImage class="absolute inset-0 h-full w-full object-cover" /> -->
        <img class="h-800" alt="Become an AFB membver today" src='@/assets/img/Dog-Sideways-Glare-1024x1024.png'>

      </div>
    </div>
  </template>

  <script setup lang="ts">
  import { HomeIcon } from '@heroicons/vue/20/solid';
</script>

<style scoped>
</style>
