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
              <router-link :to="{ name: 'DashboardView' }"> <HomeIcon class="h-10 w-full" /> </router-link>
              <h2 class="mt-8 text-2xl font-bold leading-9 tracking-tight text-gray-900">Sign in to your account</h2>
              <p class="mt-2 text-sm leading-6 text-gray-500">
                Not a member?
                &nbsp;
                <router-link :to="{ name: 'AboutView' }" class="font-semibold text-indigo-600 hover:text-indigo-500"> Register </router-link>
              </p>
            </div>

            <div class="mt-10">
              <div>
                <form action="#" method="POST" class="space-y-6">
                  <div>
                    <label for="email" class="block text-sm font-medium leading-6 text-gray-900">Email address</label>
                    <div class="mt-2">
                      <input id="email" name="email" type="email" autocomplete="email" required="" class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                    </div>
                  </div>

                  <div>
                    <label for="password" class="block text-sm font-medium leading-6 text-gray-900">Password</label>
                    <div class="mt-2">
                      <input id="password" name="password" type="password" autocomplete="current-password" required="" class="block w-full rounded-md border-0 py-1.5 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6" />
                    </div>
                  </div>

                  <div class="flex items-center justify-between">
                    <div class="flex items-center">
                      <input id="remember-me" name="remember-me" type="checkbox" class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
                      <label for="remember-me" class="ml-3 block text-sm leading-6 text-gray-700">Remember me</label>
                    </div>

                    <div class="text-sm leading-6">
                      <a href="#" class="font-semibold text-indigo-600 hover:text-indigo-500">Forgot password?</a>
                    </div>
                  </div>

                  <div>
                    <button type="submit" class="flex w-full justify-center rounded-md bg-indigo-600 px-3 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600">Sign in</button>
                  </div>
                </form>
              </div>

              <!--
              <div class="mt-10">
                <div class="relative">
                  <div class="absolute inset-0 flex items-center" aria-hidden="true">
                    <div class="w-full border-t border-gray-200" />
                  </div>
                  <div class="relative flex justify-center text-sm font-medium leading-6">
                    <span class="bg-white px-6 text-gray-900">Or continue with</span>
                  </div>
                </div>
              </div>
            -->

            </div>
          </div>
        </div>
        <div class="relative hidden w-0 flex-1 lg:block">
          <!-- <CatHeartImage class="absolute inset-0 h-full w-full object-cover" /> -->
          <img alt="Become an AFB membver today" src='@/assets/img/Cat-Heart-680x800-1.png'>
        </div>
      </div>
  </template>

<script setup lang="ts">
import { HomeIcon } from '@heroicons/vue/20/solid';
</script>

<style scoped>
</style>
