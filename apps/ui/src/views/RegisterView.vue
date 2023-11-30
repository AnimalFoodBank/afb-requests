
<script setup lang="ts">
import RegistrationVueform from '@/components/forms/RegistrationVueform.vue';
import { HomeIcon } from '@heroicons/vue/20/solid';
import { onMounted } from 'vue';

onMounted(async () => {

});

// @see List of icons: https://unpkg.com/browse/@heroicons/vue@2.0.18/24/outline/
</script>

<template>
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
            <router-link :to="{ name: 'LoginView' }" class="font-semibold text-indigo-600 hover:text-indigo-500">Login</router-link>
          </p>
        </div>

        <div class="mt-10">
          <!--
            @see https://vueform.com/docs/breaking-forms-into-steps
          -->
          <RegistrationVueform foo="test1" :bar="100">
          </RegistrationVueform>

        </div>
        <div>
            <hr class="mt-12" />
            <p class="mt-2 text-sm leading-6 text-gray-500">
              Looking for
              <router-link :to="{ name: '' }" class="font-semibold text-slate-600 hover:text-slate-500">volunteer sign-up</router-link>?
            </p>
        </div>

      </div>
    </div>
    <div class="relative hidden w-0 flex-1 lg:block">
      <!-- <CatHeartImage class="absolute inset-0 h-full w-full object-cover" /> -->
      <!-- <img class="h-800" alt="Become an AFB member today" src='@/assets/img/Dog-Sideways-Glare-1024x1024.png'> -->
      <img class="h-800" alt="Become an AFB member today" src='@/assets/img/Grey-Cat-680x600-1.png'>
    </div>
  </div>
</template>


<style scoped>
</style>

<!--

  Available Validation Rules
  @see https://vueform.com/docs/validating-elements#available-validation-rules

  Accepted
  Active URL
  After (Date)
  After Or Equal (Date)
  Alpha
  Alpha Dash
  Alpha Numeric
  Array
  Before (Date)
  Before Or Equal (Date)
  Between
  Boolean
  Confirmed
  Date
  Date Equals
  Date Format
  Different
  Digits
  Digits Between
  Dimensions (Image Files)
  Distinct
  Email
  Exists (Database)
  File
  Filled
  Greater Than
  Greater Than Or Equal
  Image
  In
  In Array
  Integer
  IP Address
  IPv4
  IPv6
  JSON
  Less Than
  Less Than Or Equal
  Max
  MIME Types
  MIME Types By File Extension
  Min
  Not In
  Not Regex
  Nullable
  Numeric
  Regular Expression
  Required
  Same
  Size
  String
  Timezone
  Unique (Database)
  URL
  UUID

-->
