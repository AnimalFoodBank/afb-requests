<script setup lang="ts">

const props = defineProps<{
  validate: (state: any) => { path: string; message: string }[]
  onSubmit: (state: any) => void
  state: {
    name: string
    email: string
    username: string
    avatar: string
    bio: string
    password_current: string
    password_new: string
  }
}>()


</script>

<template>

  <UForm :state="state" :validate="validate" :validate-on="['submit']" @submit="onSubmit">
    <UDashboardSection title="Profile" description="This information will be displayed publicly so be careful what you share.">
      <template #links>
        <UButton type="submit" label="Save changes" color="black" />
      </template>

      <UFormGroup
        name="name"
        label="Name"
        description="Will appear on receipts, invoices, and other communication."
        required
        class="grid grid-cols-2 gap-2 items-center"
        :ui="{ container: '' }"
      >
        <UInput v-model="state.name" autocomplete="off" icon="i-heroicons-user" size="md" />
      </UFormGroup>

      <UFormGroup
        name="email"
        label="Email"
        description="Used to sign in, for email receipts and product updates."
        required
        class="grid grid-cols-2 gap-2"
        :ui="{ container: '' }"
      >
        <UInput v-model="state.email" type="email" autocomplete="off" icon="i-heroicons-envelope" size="md" />
      </UFormGroup>

      <UFormGroup
        name="username"
        label="Username"
        description="Your unique username for logging in and your profile URL."
        required
        class="grid grid-cols-2 gap-2"
        :ui="{ container: '' }"
      >
        <UInput v-model="state.username" type="username" autocomplete="off" size="md" input-class="ps-[77px]">
          <template #leading>
            <span class="text-gray-500 dark:text-gray-400 text-sm">nuxt.com/</span>
          </template>
        </UInput>
      </UFormGroup>

      <UFormGroup
        name="bio"
        label="Bio"
        description="Brief description for your profile. URLs are hyperlinked."
        class="grid grid-cols-2 gap-2"
        :ui="{ container: '' }"
      >
        <UTextarea v-model="state.bio" :rows="5" autoresize size="md" />
      </UFormGroup>

      <UFormGroup
        name="password"
        label="Password"
        description="Confirm your current password before setting a new one."
        class="grid grid-cols-2 gap-2"
        :ui="{ container: '' }"
      >
        <UInput id="password" v-model="state.password_current" type="password" placeholder="Current password" size="md" />
        <UInput
          id="password_new"
          v-model="state.password_new"
          type="password"
          placeholder="New password"
          size="md"
          class="mt-2"
        />
      </UFormGroup>
    </UDashboardSection>
  </UForm>
</template>
