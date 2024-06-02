<script setup lang="ts">
import type { FormError, FormSubmitEvent } from "#ui/types";

useSeoMeta({
  title: "Client Signup",
});

definePageMeta({
  layout: "onboarding",
  auth: false,
});

const snackbar = useSnackbar();

const route = useRoute();
const email = route.query.email as string;

const fields = ref<any>([]);

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


onMounted(() => {
  fields.value = [
    {
      name: "name",
      type: "text",
      label: "Name",
      placeholder: "Enter your name",
    },
    {
      name: "email",
      type: "text",
      label: "Email",
      placeholder: "Enter your email",
  },
    {
      name: "phone",
      type: "text",
      label: "Phone",
      placeholder: "Enter your phone",
    },
  ];
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
    name: event.name,
    email: event.email,
    phone: event.phone,
  };
  console.log("Payload:", payload);

  // Send post request to the API endpoint using Nuxt 3 useFetch
  const path = "/api/v1/register/";
  const { data, pending, error, refresh } = await useFetch(path, {
    method: "POST",
    body: JSON.stringify(payload),
    headers: {
      "Content-Type": "application/json",
    },
  });

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
               :submit-button="{ trailingIcon: 'i-heroicons-arrow-right-20-solid', label: 'Create account' }"
               :loading="false"
               @submit="onSubmit">

      <template #description>
        Let's create an account for you to get started. We'll send you an email to confirm.
      </template>

      <template #validation>
        <p class="ui.validation">
          By creating an account, you agree to our
          <NuxtLink to="/legal/terms"
                    class="text-primary font-medium">Terms of Service</NuxtLink> and
          <NuxtLink to="/legal/privacy"
                    class="text-primary font-medium">Privacy Notice</NuxtLink>.
        </p>
      </template>

      <template #footer>
        <p class="ui.footer italic">
          Or <NuxtLink to="/welcome/volunteers"
                    class="text-secondary underline font-medium">signup as a Volunteer</NuxtLink>.
        </p>
      </template>
    </UAuthForm>
  </UCard>
</template>
