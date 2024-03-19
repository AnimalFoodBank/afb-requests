<script setup lang="ts">
import axios from "axios";
import { onMounted, ref } from "vue";

const builder$ = ref(null)

definePageMeta({
  layout: "dashboard",
  auth: {
    authenticated: true,
  },
});

onMounted(async () => {
  const requestForm = (await axios.get("/forms/requestform.ts")).data;
  console.log(typeof requestForm.builder, typeof requestForm.history)
  let builderObject = requestForm.builder; // object
  let history = requestForm.history; // array

  (builder$.value as any)?.load(builderObject, history);
});
</script>

<template>
  <UDashboardPage>
    <UDashboardPanel>
      <UDashboardNavbar title="Dashboard"> </UDashboardNavbar>

      <UDashboardPanelContent class="h-screen">
        <ClientOnly>
          <VueformBuilder ref="builder$" />
        </ClientOnly>
      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>
</template>
