<template>
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <template #header>
      <h1 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-gray-50">Contact Us</h1>
    </template>

    <Vueform
    size="lg"
    endpoint="/api/v1/contact"
    method="POST"
  >
    <TextElement
      name="email"
      input-type="email"
      :rules="[
        'required',
        'email',
      ]"
      label="Email"
    />
    <TextElement
      name="name"
      label="Name"
      info="Your name"
    />
    <SelectElement
      name="topic"
      :search="true"
      :native="false"
      input-type="search"
      autocomplete="off"
      label="Topic"
      info="Optional"
      :items="[
        {
          value: 'feedback',
          label: 'General Feedback',
        },
        {
          value: 'help',
          label: 'Updating address',
        },
      ]"
    />
    <TextareaElement
      name="textarea"
      label="Message"
    />
    <ButtonElement
      name="submit"
      button-label="Submit"
      :submits="true"
      align="right"
      size="lg"
      :full="true"
    />
  </Vueform>

    <template #footer>

    </template>
  </UCard>


</template>


<script setup lang="ts">
  // import type { ContactFormState } from '@/types/index';

  import type { FormError, FormSubmitEvent } from "#ui/types";

  useSeoMeta({
    title: "Contact Us",
  });

  const config = useRuntimeConfig();


  // Auth
  //
  // Note: You cannot use local protection when you turned on the global
  // middleware by setting globalAppMiddleware: true in the nuxt-auth
  // configuration. You will get an error along the lines of "Error: Unknown
  // route middleware: 'auth'". This is because the auth middleware is then
  // added globally and not available to use as a local, page-specific
  // middleware.

  definePageMeta({
    layout: "onboarding",
    auth: false,
  });

  const fields = [
    {
      name: "email",
      type: "text",
      placeholder: "Your email address",
      icon: "i-heroicons-envelope",
      autofocus: true,
    },
  ];


  const validateEmail = (email: string) => {
    return (/^\w+([\.-\\+]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))
  }

  const validate = (state: any): FormError[] => {
    const errors = []
    if (!state.email) errors.push({ path: 'email', message: 'Email is required' })
    if (!validateEmail(state.email)) {
      errors.push({ path: 'email', message: 'Please enter a valid email address' })
    }

    return errors
  }

  async function onSubmit(
    event: FormSubmitEvent<{
      email: string;
    }>,
  ) {
    console.log("Submitted", event);
  }

  </script>
