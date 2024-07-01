<script setup lang="ts">
const route = useRoute()
const appConfig = useAppConfig()
const { isHelpSlideoverOpen } = useDashboard()

const links = [
  {
    id: 'home',
    label: 'Portal Home',
    icon: 'i-heroicons-home',
    to: '/dashboard',
    tooltip: {
      text: 'Home',
    }
  },
  {
    id: 'requests',
    label: 'Requests',
    icon: 'i-ph-phone',
    defaultOpen: route.path.startsWith('/requests'),
    to: '/requests',
    //children: [
    //  {
    //    label: 'Request History',
    //    to: '/requests',
    //    exact: true
    //  },
    //  {
    //    label: 'New Request',
    //    to: '/requests/new',
    //    exact: true
    //  },
    //],

    tooltip: {
      text: 'Your history of requests',
    }
  },
  {
    id: 'profile',
    label: 'Profile',
    to: '/profile',
    icon: 'i-heroicons-user',
    //children: [
    //  {
    //    label: 'Address',
    //    to: '/profile',
    //    exact: true
    //  },
    //  {
    //    label: 'Pets',
    //    to: '/profile/pets',
    //    exact: true
    //  },
    //],
    tooltip: {
      text: 'Your profile details',
    }
  }
]

const footerLinks = [{
  label: 'Help & Support',
  icon: 'i-heroicons-question-mark-circle',
  to: '/contact',
  target: '_blank',
}]


const defaultColors = ref(['green', 'teal', 'cyan', 'sky', 'blue', 'indigo', 'violet'].map(color => ({ label: color, chip: color, click: () => appConfig.ui.primary = color })))
const colors = computed(() => defaultColors.value.map(color => ({ ...color, active: appConfig.ui.primary === color.label })))
</script>

<template>

  <UDashboardLayout>
    <UDashboardPanel :width="250" :resizable="{ min: 200, max: 300 }" collapsible>
      <UDashboardNavbar class="!border-transparent" :ui="{ left: 'flex-1' }">
        <template #left>
          <NuxtLink to="/">
            <Logo />
          </NuxtLink>
        </template>
      </UDashboardNavbar>

      <UDashboardSidebar>
        <UDashboardSidebarLinks :links="links" />

        <div class="flex-1" />

        <UDashboardSidebarLinks :links="footerLinks" />

        <UDivider class="sticky bottom-0" />

        <template #footer>
          <!-- ~/components/UserDropdown.vue -->
          <UserDropdown />
        </template>
      </UDashboardSidebar>
    </UDashboardPanel>

    <slot />

    <!-- ~/components/HelpSlideover.vue -->
    <!-- <HelpSlideover /> -->
    <!-- ~/components/NotificationsSlideover.vue -->
    <!-- <NotificationsSlideover /> -->
  </UDashboardLayout>

</template>
