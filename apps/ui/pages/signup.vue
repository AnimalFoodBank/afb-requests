<!--
  This is a Vue page for the signup functionality.
It uses the 'definePageMeta' function to set the page metadata.
-->

<script setup lang="ts">

definePageMeta({
  layout: 'onboarding',
  auth: false,
})

useSeoMeta({
  title: 'Sign up'
})

const fields = [{
  name: 'name',
  type: 'text',
  label: 'Name',
  placeholder: 'Enter your name'
}, {
  name: 'email',
  type: 'text',
  label: 'Email',
  placeholder: 'Enter your email'
}, {
  name: 'password',
  label: 'Password',
  type: 'password',
  placeholder: 'Enter your password'
}]

const validate = (state: any) => {
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Email is required' })
  if (!state.password) errors.push({ path: 'password', message: 'Password is required' })
  return errors
}

const providers = [{
  label: 'Continue with Gmail',
  icon: 'i-simple-icons-gmail',
  color: 'white' as const,
  click: () => {
    console.log('Redirect to Google')
  }
},{
  label: 'Continue with Apple',
  icon: 'i-simple-icons-apple',
  color: 'white' as const,
  click: () => {
    console.log('Redirect to Apple')
  }
}]

function onSubmit (data: any) {
  console.log('Submitted', data)
}
</script>

<!-- eslint-disable vue/multiline-html-element-content-newline -->
<!-- eslint-disable vue/singleline-html-element-content-newline -->
<template>
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <UAuthForm
      :fields="fields"
      :validate="validate"
      :providers="providers"
      align="top"
      title="Create an account"
      :ui="{ base: 'text-center', footer: 'text-center' }"
      :submit-button="{ label: 'Create account' }"
      @submit="onSubmit"
    >
      <template #description>
        Already have an account? <NuxtLink to="/login" class="text-primary font-medium">Login</NuxtLink>.
      </template>

      <template #footer>
        By signing up, you agree to our <NuxtLink to="/" class="text-primary font-medium">Terms of Service</NuxtLink>.
      </template>
    </UAuthForm>
  </UCard>
</template>
