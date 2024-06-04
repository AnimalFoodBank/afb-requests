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

const router = useRouter();
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
      name: "phone_number",
      type: "text",
      label: "Phone",
      placeholder: "Your phone number",
      icon: "i-heroicons-phone",
      help: "We use your phone number to coordinate deliveries. See our Privacy Notice for how we use your information (link below).",
      required: false,
    },
  ];
});


async function onSubmit(
  event: FormSubmitEvent<{
    email: string;
    name: string;
    phone_number: string;
  }>,
) {
  console.log("Submitted", event);

  // Prepare the payload
  const payload = {
    role: 'client',
    name: event.name,
    email: event.email,
    phone_number: event.phone_number,
  };
  console.log("Payload:", payload);

  // Send post request to the API endpoint using Nuxt 3 useFetch
  const path = "/api/v1/register/";

  try {

    const data = await $fetch(path, {
      method: "POST",
      body: JSON.stringify(payload),
      headers: {
        "Content-Type": "application/json",
      },
    });

    await navigateTo("/dashboard");

  } catch (error: any) {
    const data = error.data;

    if (data && data.email) {
      snackbar.add({
        type: "error",
        text: "Please choose another email address",
      });

    } else {

      throw createError({
        statusCode: 404,
        statusMessage: 'Page Not Found',
        fatal: true
      })
    }
  }

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
