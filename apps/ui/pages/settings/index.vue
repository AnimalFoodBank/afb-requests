<script setup lang="ts">
import type { FormError, FormSubmitEvent } from '#ui/types';

const fileRef = ref<{ input: HTMLInputElement }>()
const isDeleteAccountModalOpen = ref(false)

const state = reactive({
  name: 'Delbo Baggins',
  email: 'delbo@solutious.com',
  address: 'delbob',
  avatar: '',
  bio: '',
  password_current: '',
  password_new: ''
})

const toast = useToast()

function validate (state: any): FormError[] {
  const errors = []
  if (!state.name) errors.push({ path: 'name', message: 'Please enter your name.' })
  if (!state.email) errors.push({ path: 'email', message: 'Please enter your email.' })
  if ((state.password_current && !state.password_new) || (!state.password_current && state.password_new)) errors.push({ path: 'password', message: 'Please enter a valid password.' })
  return errors
}

function onFileChange (e: Event) {
  const input = e.target as HTMLInputElement

  if (!input.files?.length) {
    return
  }

  state.avatar = URL.createObjectURL(input.files[0])
}

function onFileClick () {
  fileRef.value?.input.click()
}

async function onSubmit (event: FormSubmitEvent<any>) {
  // Do something with data
  console.log(event.data)

  toast.add({ title: 'Profile updated', icon: 'i-heroicons-check-circle' })
}
</script>

<template>
  <UDashboardPanelContent class="pb-24">
    <UDashboardSection title="Theme" description="">
      <template #links>
        <UColorModeSelect color="gray" />
      </template>
    </UDashboardSection>

    <UDivider class="mb-4" />

    <UForm :state="state" :validate="validate" :validate-on="['submit']" @submit="onSubmit">
      <UDashboardSection title="Profile" description="">
        <template #links>
          <UButton type="submit" label="Save changes" color="black" />
        </template>

        <UFormGroup
          name="name"
          label="Name"
          description="."
          required
          class="grid grid-cols-2 gap-2 items-center"
          :ui="{ container: '' }"
        >
          <UInput v-model="state.name" autocomplete="off" icon="i-heroicons-user" size="md" />
        </UFormGroup>

        <UFormGroup
          name="email"
          label="Email"
          description="."
          required
          class="grid grid-cols-2 gap-2"
          :ui="{ container: '' }"
        >
          <UInput v-model="state.email" type="email" autocomplete="off" icon="i-heroicons-envelope" size="md" disabled />
        </UFormGroup>

        <UFormGroup
          name="address"
          label="Address"
          description="."
          required
          class="grid grid-cols-2 gap-2"
          :ui="{ container: '' }"
        >
          <UInput v-model="state.address" type="address" autocomplete="off" icon="i-heroicons-home" size="md" disabled>
            <template #trailing>
              <span class="text-gray-500 dark:text-gray-400 text-sm">H0H 0H0</span>
            </template>
          </UInput>
        </UFormGroup>

        <UFormGroup name="avatar" label="Photo" class="grid grid-cols-2 gap-2" help="JPG, GIF or PNG. 1MB Max." :ui="{ container: 'flex flex-wrap items-center gap-3', help: 'mt-0' }">
          <UAvatar :src="state.avatar" :alt="state.name" size="lg" />

          <UButton label="Choose" color="white" size="md" @click="onFileClick" />

          <UInput ref="fileRef" type="file" class="hidden" accept=".jpg, .jpeg, .png, .gif" @change="onFileChange" />
        </UFormGroup>

        <UFormGroup
          name="bio"
          label="Pets"
          description="."
          class="grid grid-cols-2 gap-2"
          :ui="{ container: '' }"
        >
          <UTextarea v-model="state.bio" :rows="5" autoresize size="md" />
        </UFormGroup>

      </UDashboardSection>
    </UForm>

    <!-- ~/components/settings/DeleteAccountModal.vue -->
    <SettingsDeleteAccountModal v-model="isDeleteAccountModalOpen" />
  </UDashboardPanelContent>
</template>
