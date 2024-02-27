<script setup lang="ts">
import { sub } from 'date-fns';
import type { Period, Range } from '~/types';

definePageMeta({
  layout: 'dashboard',
  auth: {
    unauthenticatedOnly: false,
  },
  // colorMode: 'dark',
})

const { isNotificationsSlideoverOpen } = useDashboard()

const items = [[{
  label: 'New mail',
  icon: 'i-heroicons-paper-airplane',
  to: '/inbox'
}, {
  label: 'New user',
  icon: 'i-heroicons-user-plus',
  to: '/users'
}]]

const range = ref<Range>({ start: sub(new Date(), { days: 14 }), end: new Date() })
const period = ref<Period>('daily')
</script>

<template>
  <UDashboardPage>
    <UDashboardPanel grow>
      <UDashboardNavbar title="Dashboard">

      </UDashboardNavbar>

      <UDashboardToolbar>
      </UDashboardToolbar>

      <UDashboardPanelContent>
      </UDashboardPanelContent>
    </UDashboardPanel>
  </UDashboardPage>
</template>
