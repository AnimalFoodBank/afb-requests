<script setup lang="ts">
import type { FormError, FormSubmitEvent } from "#ui/types";

useSeoMeta({
  title: "Volunteer Signup",
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
    label: "Phone*",
    placeholder: "Your phone number",
    icon: "i-heroicons-phone",
    help: "We require a phone number for verification. You will also be able to receive SMS notifications at this number if you choose to.",
  },
  {
    name: "intro",
    type: "textarea",
    label: "What's a funny name for a pet?",
    placeholder: "e.g. I met a turtle named 'Jazz' once",
    icon: "i-ph-signature",
    required: false,
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

  if (!validateEmail(state.email))
    errors.push({ path: 'email', message: 'Please enter a valid email address' });

  if (!state.phone)
    errors.push({ path: "phone", message: "Phone is required" });

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
    intro: string;
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
               title="Volunteer Signup"
               description="Enter a few details to get started."
               align="top"
               icon="i-ph-hand-heart-fill"
               :ui="{ base: 'text-center', footer: 'text-center' }"
               :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid', label: 'Create account' }"
               :loading="false"
               @submit="onSubmit">

      <template #description>
        Let's create an account for you to get started. All volunteer accounts are reviewed by AFB Staff before being approved.
      </template>

      <template #validation>
        <p class="ui.footer font-medium">
          By creating an account, you agree to our
          <NuxtLink to="/legal/volunteers"
                    class="text-primary">Volunteer Agreement</NuxtLink>,
          <NuxtLink to="/legal/terms"
                    class="text-primary">Terms of Service</NuxtLink> and
          <NuxtLink to="/legal/privacy"
                    class="text-primary">Privacy Notice</NuxtLink>.
        </p>
      </template>
    </UAuthForm>
  </UCard>
</template>
