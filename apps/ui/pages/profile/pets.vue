

<template>
  <UDashboardPanelContent class="pb-24">
    <UDashboardSection title="Theme" description="">
      <template #links>
        <UColorModeSelect color="gray" />
      </template>
    </UDashboardSection>

    <UDivider class="mb-4" />

    <UForm :state="state" :validate="validate" :validate-on="['submit']" @submit="onSubmit">

    </UForm>

  </UDashboardPanelContent>
</template>
