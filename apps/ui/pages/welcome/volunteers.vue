<script setup lang="ts">
import type { FormError, FormSubmitEvent } from "#ui/types";

useSeoMeta({
  title: "Become a Volunteer",
});

definePageMeta({
  layout: "onboarding",
  auth: false,
});


const fields = [
  {
    name: "name",
    type: "text",
    label: "Name",
    placeholder: "e.g. first name, full name or a nickname",
    icon: "i-heroicons-user-circle",
    autofocus: true,
  },
  {
    name: "location",
    type: "text",
    label: "City",
    placeholder: "Where are you based?",
    icon: "i-ph-map-pin-area",
    required: false,
  },
  {
    name: "intro",
    type: "textarea",
    label: "Favourite name for a pet",
    placeholder: "What is your favourite pet name?",
    icon: "i-ph-pencil-circle-fill",
    autofocus: false,
  },
  {
    name: "email",
    type: "text",
    label: "Email",
    placeholder: "Your email address",
    icon: "i-heroicons-envelope",
    autofocus: false,
  },
];

const validate = (state: any): FormError[] => {
  const errors = [];
  if (!state.name)
    errors.push({ path: "name", message: "Name is required" });

  if (!state.email)
      errors.push({ path: "email", message: "Email is required" });

  if (!state.location)
      errors.push({ path: "location", message: "City is required" });

  if (!state.intro)
      errors.push({ path: "intro", message: "Intro is required" });

  return errors;
};

let timeoutId: number | undefined;

onUnmounted(() => {
  if (timeoutId) {
    clearTimeout(timeoutId);
  }
});

async function onSubmit(
  event: FormSubmitEvent<{
    email: string;
  }>,
) {
  console.log("Submitted", event);

  // Prepare the payload
  const payload = {
    email: event.email,
  };
  console.log("Payload:", payload);

}

const defaultBranch = ref("none");
</script>

<!-- eslint-disable vue/multiline-html-element-content-newline -->
<!-- eslint-disable vue/singleline-html-element-content-newline -->
<template>
  <NuxtSnackbar top left shadow :duration="10000" />
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <!-- https://ui.nuxt.com/pro/components/auth-form -->

    <UAuthForm
      :fields="fields"
      :validate="validate"
      title="Become a Volunteer"
      description="Enter a few details to get started."
      align="top"
      icon="i-ph-hand-heart-fill"
      :ui="{ base: 'text-center', footer: 'text-center' }"
      :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid' }"
      :loading="false"
      @submit="onSubmit"
    >
      <template #description>
        Let's create an account for you to get started. We'll send you an email to confirm your account.

      </template>

      <template #footer>
        By signing in, you agree to our
        <NuxtLink to="/legal/terms" class="text-primary font-medium"
          >Terms of Service</NuxtLink
        >.
      </template>
    </UAuthForm>
  </UCard>
</template>
