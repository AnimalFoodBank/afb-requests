
<script setup lang="ts">

const props = defineProps<{
  title?: String
  description?: String
  requests?: Array<FoodRequest>
  cta?: Boolean
}>()

// A list of all the users in your account including their name, title, email and role.
</script>

<template>

  <div class="px-4 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold leading-6 text-gray-900 dark:text-gray-50">{{ title }}</h1>
        <p class="mt-2 text-sm text-gray-700 dark:text-gray-200">{{ description }}</p>
      </div>
      <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
        <a v-if="cta" type="button" href="/requests/new"
                class="block rounded-md bg-primary px-3 py-2 text-center text-sm font-semibold text-white dark:text-black shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 ">
                Request Pet Food
        </a>
      </div>
    </div>
    <!-- {
  "address_text": "1201 Kingsway, Med Hat",
  "address_google_place_id": null,
  "address_canadapost_id": null,
  "address_latitude": null,
  "address_longitude": null,
  "address_buildingtype": "NOT_SPECIFIED",
  "address_details": {},
  "contact_phone": "+12507772171",
  "contact_email": "",
  "contact_name": "Pearl",
  "method_of_contact": "Email",
  "pet_details": {},
  "confirm_correct": true,
  "accept_terms": true,
  "date_requested": "2024-04-06"
} -->
    <div class="-mx-4 mt-8 sm:-mx-0">
      <table class="min divide-y divide-gray-300 dark:divide-gray-300">
        <thead>
          <tr>
            <th scope="col" class="hidden py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 dark:text-white lg:table-cell sm:pl-0 ">Date</th>
            <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 dark:text-white lg:table-cell">Contact</th>
            <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 dark:text-white lg:table-cell">Address</th>
            <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900 dark:text-white sm:table-cell sm:pl-0 ">Contents</th>
            <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0"><span class="sr-only">View</span></th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 bg-white dark:bg-slate-900 dark:divide-gray-500">
          <tr v-for="request in requests" :key="request.id">
            <td class="max-w-sm w-full py-4 pl-4 pr-3 text-sm font-medium text-gray-900 dark:text-white sm:w-auto sm:max-w-none sm:pl-0">
              {{ request.date_requested }}
              <dl class="font-normal lg:hidden">
                <dt class="sr-only">Contact</dt>
                <dd class="mt-1 truncate text-gray-900 dark:text-gray-200">{{ request.contact_name }}</dd>
                <dt class="sr-only">Contents</dt>
                <dd class="mt-1 truncate text-gray-900 dark:text-gray-200">{{ request.pet_details.pets_blob }}</dd>
                <dt class="sr-only">Address</dt>
                <dd class="mt-1 truncate text-gray-500 dark:text-gray-200">{{ request.address_text }}</dd>
              </dl>
            </td>
            <td class="max-w-xs hidden px-3 py-4 text-sm text-gray-500 dark:text-gray-200 lg:table-cell">{{ request.contact_name }}</td>
            <td class="max-w-xs hidden px-3 py-4 text-sm text-gray-500 dark:text-gray-200 lg:table-cell">{{ request.address_text }}</td>
            <td class="max-w-xs hidden px-3 py-4 text-sm text-gray-500 dark:text-gray-200 lg:table-cell">{{ request.pet_details.pets_blob }}</td>
            <td class="py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
            <a :href="`/requests/${request.id}/details`" class="text-indigo-600 hover:text-indigo-900 dark:text-blue-400">View<span class="sr-only">, {{ request.name
                  }}</span></a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
