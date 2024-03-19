<script setup lang="ts">
const model = defineModel({
  type: Boolean
})

const toast = useToast()

const loading = ref(false)

function onDelete () {
  loading.value = true

  setTimeout(() => {
    loading.value = false
    toast.add({ icon: 'i-heroicons-check-circle', title: 'Your account has been dewormed', color: 'red' })
    model.value = false
  }, 2000)
}
</script>

<template>
  <UDashboardModal
    v-model="model"
    title="Dangerous action (example)"
    description="Are you sure you want to deworm your account? NOTE: This action does not do anything. It's just an example."
    icon="i-heroicons-exclamation-circle"
    prevent-close
    :close-button="null"
    :ui="{
      icon: {
        base: 'text-red-500 dark:text-red-400'
      } as any,
      footer: {
        base: 'ml-16'
      } as any
    }"
  >
    <template #footer>
      <UButton color="red" label="Deworm" :loading="loading" @click="onDelete" />
      <UButton color="white" label="Cancel" @click="model = false" />
    </template>
  </UDashboardModal>
</template>
