<script setup lang="ts">

const props = defineProps<{
  title?: String
  description?: String
  state?: Object
  cta?: Boolean
  icon?: String
}>()


const errors = ref<FormError[]>([])
const toast = useToast()

function validate (state: any): FormError[] {
  const errors = []
  if (!state.name) errors.push({ path: 'name', message: 'Please enter your name.' })
  if (!state.email) errors.push({ path: 'email', message: 'Please enter your email.' })
  if (!state.branch_selection) errors.push({ path: 'branch_selection', message: 'Please doublecheck branch location.' })
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
        <UDashboardSection :title="title" :description="description" :icon="icon">
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
            <!-- <USelect v-model="state.branch_selection" name="branch_selection" icon="i-ph-map-pin" :options="branchLocations" option-attribute="text" class=""/> -->
            <UInput type="select" name="branch_selection" v-model="state.branch_selection" autocomplete="off" icon="i-ph-map-pin" size="md" disabled />

            <p class="text-gray-500 text-xs italic">Please contact admin@animalfoodbank.org to update your branch.</p>
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
            name="email"
            label="Your Email"
            description="The email address you use to sign in. We also use this for co-ordinating food requests."
            class="grid grid-cols-2 gap-2 items-center"
            :ui="{ container: '' }"
          >
            <UInput v-model="state.email" autocomplete="off" icon="i-heroicons-envelope" size="md" disabled />
          </UFormGroup>

          <UFormGroup
            name="name"
            label="Your Phone (optional)"
            description="Please enter your name."
            class="grid grid-cols-2 gap-2 items-center"
            :ui="{ container: '' }"
          >
            <UInput v-model="state.phone" autocomplete="off" icon="i-heroicons-phone" size="md" />
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
