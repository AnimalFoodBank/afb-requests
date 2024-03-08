<script setup lang="ts">

const props = defineProps<{
  title?: String
  description?: String
  state?: Object
  cta?: Boolean
}>()


const errors = ref<FormError[]>([])
const toast = useToast()


function validate (state: any): FormError[] {
  const errors = []
  if (!state.name) errors.push({ path: 'name', message: 'Please enter your name.' })
  if (!state.email) errors.push({ path: 'email', message: 'Please enter your email.' })
  if ((state.password_current && !state.password_new) || (!state.password_current && state.password_new)) errors.push({ path: 'password', message: 'Please enter a valid password.' })
  return errors
}

async function onSubmit (event: FormSubmitEvent<any>) {
  // Do something with data
  console.log(event.data)

  toast.add({
    title: `${props.title} updated`,
    icon: 'i-heroicons-check-circle',
  })
}

</script>

<template>
    <div>
      <UForm :state="state" :validate="validate" :validate-on="['submit']" @submit="onSubmit">
        <UDashboardSection :title="title" :description="description" icon="i-ph-paw-print">
          <template #links v-if="cta">
            <UButton type="submit" label="Save changes" color="black" />
          </template>

          <UFormGroup
            name="pets"
            label="Pets"
            description="The pets in your household"
            class="grid grid-cols-2 gap-2"
            :ui="{ container: '' }"
          >
            <ul role="list" class="divide-y divide-gray-100 dark:divide-gray-700">
              <li v-for="petDetails in state.pets" :key="petDetails" class="flex justify-between gap-x-6 py-5">
                <div class="flex">
                  <div class="flex-auto">
                    <p class="text-sm font-semibold leading-6 text-gray-900 dark:text-gray-100">{{ petDetails.name }}</p>
                    <p class="mt-1 truncate text-xs leading-5 text-gray-500 dark:text-gray-200">{{ petDetails.type }}</p>
                    <UTextarea :rows="5" autoresize size="lg" :placeholder="petDetails.details" />
                  </div>
                </div>
              </li>
            </ul>
          </UFormGroup>

        </UDashboardSection>
      </UForm>

    </div>
  </template>
