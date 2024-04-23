<script setup lang="ts">


useSeoMeta({
  title: "Sign In",
})

const config = useRuntimeConfig();
const snackbar = useSnackbar();

definePageMeta({
  layout: 'onboarding',
  auth: false,
})


</script>

<template>
  <NuxtSnackbar top
                left
                shadow
                :duration="10000" />

  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">

      <div class="w-full max-w-sm space-y-6 text-center">
        <UIcon name="i-heroicons-inbox-arrow-down" class="mx-auto w-24 h-24" />
        <h2 class="text-2xl text-gray-900 dark:text-white font-bold text-center">Check your Inbox</h2>
        <p class="text-gray-500 dark:text-gray-400 text-center">Didn't get an email? <NuxtLink to="/login" class="text-primary font-medium">Try again</NuxtLink>.</p>
      </div>

  </UCard>
</template>
