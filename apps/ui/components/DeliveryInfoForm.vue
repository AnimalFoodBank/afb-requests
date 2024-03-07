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
        <UDashboardSection :title="title" :description="description" icon="i-heroicons-user">
          <template #links v-if="cta">
            <UButton type="submit" label="Save changes" color="black" />
          </template>

          <UFormGroup
            name="branch"
            label="AFB Branch"
            description="The location that will fulfill your request."
            required
            class="grid grid-cols-2 gap-2"
            :ui="{ container: '' }"
          >
            <UInput v-model="state.branch" type="branch" autocomplete="off" icon="i-heroicons-tree" size="md" >
            </UInput>
            <p class="text-gray-500 text-xs italic">Please contact admin@animalfoodbank.org to update.</p>

          </UFormGroup>

          <UFormGroup
            name="name"
            label="Your Name"
            description="Please enter your name."
            required
            class="grid grid-cols-2 gap-2 items-center"
            :ui="{ container: '' }"
          >
            <UInput v-model="state.name" autocomplete="off" icon="i-heroicons-user" size="md" />
          </UFormGroup>

          <UFormGroup
            name="address"
            label="Address"
            description="The address for the pet food delivery."
            required
            class="grid grid-cols-2 gap-2"
            :ui="{ container: '' }"
          >
            <UInput v-model="state.address" type="address" autocomplete="off" icon="i-heroicons-envelope" size="md" disabled>
              <template #trailing>
                <span class="text-gray-500 dark:text-gray-400 text-sm">H0H 0H0</span>
              </template>
            </UInput>
          </UFormGroup>

        </UDashboardSection>
      </UForm>

    </div>
  </template>
