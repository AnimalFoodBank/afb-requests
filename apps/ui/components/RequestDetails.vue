<!-- https://tailwindui.com/components/application-ui/data-display/description-lists -->

<script setup lang="ts">

const props = defineProps({
  requestDetails: { type: Object, required: true },
  // model: { type: Object, required: true }
})

</script>

<template>
  <div>

    <div class="mt-6 border-t border-gray-100">
      <dl class="divide-y divide-gray-100">
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Contact Info</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ requestDetails.contact_name }} ({{ requestDetails.contact_phone }})<p>{{ requestDetails.contact_email }}</p></dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Pets</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">{{ requestDetails.pet_details?.pets_blob  }}</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Email address</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0">margotfoster@example.com</dd>
        </div>
        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Status</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0 text-wrap">
            {{ requestDetails.status }}
          </dd>
        </div>

        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Address</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0 text-wrap">
            <p>{{ requestDetails.address_text }}</p>
            <p>{{ requestDetails.address_buildingtype }}</p>
            <p>{{ requestDetails.address_details }}</p>
            <p>{{ requestDetails.address_google_place_id }}</p>
            <p>{{ requestDetails.address_canadapost_id }}</p>
            <p>{{ requestDetails.address_latitude }}, {{requestDetails.longitude}}</p>
          </dd>
        </div>

        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Safe Drop</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0 text-wrap">
            <p>Agree: {{ requestDetails.safe_drop_agree }}</p>
            <p>{{ requestDetails.safe_drop_instructions }}</p>
          </dd>
        </div>

        <div class="px-4 py-6 sm:grid sm:grid-cols-3 sm:gap-4 sm:px-0">
          <dt class="text-sm font-medium leading-6 text-gray-900">Agreements</dt>
          <dd class="mt-1 text-sm leading-6 text-gray-700 sm:col-span-2 sm:mt-0 text-wrap">
            <p>terms of use: {{ requestDetails.accept_terms }}</p>
            <p>confirm correct: {{ requestDetails.confirm_correct }}</p>
          </dd>
        </div>

      </dl>
    </div>
  </div>
</template>
