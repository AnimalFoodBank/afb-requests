<script setup lang="ts">
import type { FormError, FormSubmitEvent } from "#ui/types";

useSeoMeta({
  title: "Client Signup",
});

definePageMeta({
  layout: "onboarding",
  auth: false,
});


const fields = [
  {
    name: "name",
    type: "text",
    label: "Name*",
    placeholder: "e.g. first name, full name or a nickname",
    icon: "i-heroicons-user-circle",
    autofocus: true,
  },
  {
    name: "email",
    type: "text",
    label: "Email*",
    placeholder: "Your email address",
    icon: "i-heroicons-envelope",
  },
  {
    name: "phone",
    type: "text",
    label: "Phone",
    placeholder: "Your phone number",
    icon: "i-heroicons-phone",
    help: "If you provide a phone number, we will use it to coordinate your delivery.",
  },
];

const validateEmail = (email: string) => {
  return (/^\w+([\.-\\+]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(email))
}

const validate = (state: any): FormError[] => {
  const errors = [];
  if (!state.name)
    errors.push({ path: "name", message: "Name is required" });

  if (!state.email)
    errors.push({ path: "email", message: "Email is required" });

  if (!validateEmail(state.email)) {
    errors.push({ path: "email", message: "Please enter a valid email address" });
  }

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
    name: string;
    phone: string;
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
  <NuxtSnackbar top
                left
                shadow
                :duration="10000" />

  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">

    <UAuthForm :fields="fields"
               :validate="validate"
               title="Client Signup"
               icon="i-ph-paw-print-fill"
               :ui="{ base: 'text-center', footer: 'text-center' }"
               :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid' }"
               :loading="false"
               @submit="onSubmit">
      <template #description>
        Let's create an account for you to get started. We'll send you an email to confirm your account.
      </template>

      <template #validation>
        <p class="ui.footer">
        By signing in, you agree to our
        <NuxtLink to="/legal/terms"
                  class="text-primary font-medium">Terms of Service</NuxtLink>.
                </p>
      </template>
    </UAuthForm>
  </UCard>
</template>
