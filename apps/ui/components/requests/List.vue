
<script setup lang="ts">
import type { FoodRequest } from '~/types/models';

const props = defineProps<{
  title?: String
  description?: String
  requests?: Array<FoodRequest>
  cta?: Boolean
}>()

const visibleRequests = ref(props.requests || [])


// We define the computed value outside of onMounted to to properly
// utilize Vue's reactivity system. This will ensure that
// hasOpenRequests updates automatically when visibleRequests changes.
const hasOpenRequests = computed(() => visibleRequests.value.some(request => request.request_status !== 'delivered'))

onMounted(() => {
  console.log('requests', visibleRequests.value, hasOpenRequests.value)
})

</script>

<template>

  <div class="px-4 sm:px-6 lg:px-8">
    <div class="sm:flex sm:items-center">
      <div class="sm:flex-auto">
        <h1 class="text-base font-semibold leading-6 text-gray-900 dark:text-gray-50">{{ title }}</h1>
        <p class="mt-2 text-sm text-gray-700 dark:text-gray-200">{{ description }}</p>
      </div>
      <div class="mt-4 sm:ml-16 sm:mt-0 sm:flex-none">
        <a v-if="cta && !hasOpenRequests" type="button" href="/requests/new"
                class="block rounded-md bg-primary px-3 py-2 text-center text-sm font-semibold text-white dark:text-black shadow-sm focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 ">
                Request Pet Food
        </a>
      </div>
    </div>

    <div class="-mx-4 mt-8 sm:-mx-0">
      <table class="min-w-full divide-y divide-gray-300 dark:divide-gray-300">
        <thead>
          <tr>
            <th scope="col" class="py-3.5 pl-4 pr-3 text-left text-sm font-semibold text-gray-900 dark:text-white sm:table-cell sm:pl-0 ">Date</th>
            <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 dark:text-white sm:table-cell">Contact</th>
            <th scope="col" class="hidden px-3 py-3.5 text-left text-sm font-semibold text-gray-900 dark:text-white lg:table-cell">Contents</th>
            <th scope="col" class="px-3 py-3.5 text-left text-sm font-semibold text-gray-900 dark:text-white sm:table-cell sm:pl-0 ">Address</th>
            <th scope="col" class="relative py-3.5 pl-3 pr-4 sm:pr-0"><span class="sr-only">View</span></th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 bg-white dark:bg-gray-900 dark:divide-gray-500">
          <tr
            v-for="(request, index) in requests"
            :key="request.id"
            :class="(index === 0) ? 'bg-slate-100 dark:bg-slate-800': ''"
            >
            <td class="whitespace-nowrap py-4 pl-4 pr-3 text-sm font-medium text-gray-900 dark:text-white sm:pl-0">
              {{ request.date_requested }}
            </td>

            <td class="hidden whitespace-nowrap px-3 py-4 text-sm text-gray-500 sm:table-cell">{{ request.contact_name }}</td>
            <td class="hidden whitespace-nowrap px-3 py-4 text-sm text-gray-500 lg:table-cell">{{ request.pet_details?.pets_blob }}</td>
            <td class="whitespace-nowrap px-3 py-4 text-sm text-gray-500">{{ request.address_text }}</td>
            <td class="whitespace-nowrap py-4 pl-3 pr-4 text-right text-sm font-medium sm:pr-0">
            <a :href="`/requests/${request.id}/details`" class="text-indigo-600 hover:text-indigo-900 dark:text-blue-400">{{ request.request_status }}<span class="sr-only">, {{ request.name
                  }}</span></a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
