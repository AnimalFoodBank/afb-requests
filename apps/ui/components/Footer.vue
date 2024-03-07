<script setup lang="ts">
const links = [
  {
    label: 'Resources',
    children: [
      { label: 'About Us', to: 'https://animalfoodbank.org/about-us/' },
      { label: 'Pet Food Recovery Program', to: 'https://animalfoodbank.org/afb-national-pet-food-recovery-program/' },
      { label: 'Get Help', to: 'https://animalfoodbank.org/get-help/' },
      { label: 'AFB Pet Club', to: 'https://afbpetclub.org' },
      { label: 'Contact Us', to: 'https://animalfoodbank.org/contact-us/' },
    ]
  },
  {
    label: 'Company',
    children: [
      { label: 'Donate Now', to: 'https://animalfoodbank.org/donate-now/' },
      { label: 'Drop Off Locations', to: 'https://animalfoodbank.org/wishlist/' },
      { label: 'Wish List', to: 'https://animalfoodbank.org/wishlist/' },
      { label: 'Other Ways To Help', to: 'https://animalfoodbank.org/volunteer/' },
      { label: 'Sponsorship', to: 'https://animalfoodbank.org/sponsorship' }
    ]
  }
]

const toast = useToast()

</script>

<template>
  <UFooter>
    <template #top>
      <UFooterColumns :links="links">
        <template #right>
          <UFormGroup name="email" label="Subscribe to our newsletter" size="md">
            <UInput type="email" icon="i-heroicons-envelope">
              <template #trailing>
                <UButton type="submit" size="2xs" color="black" label="Subscribe" />
              </template>
            </UInput>
          </UFormGroup>
        </template>
      </UFooterColumns>
    </template>

    <template #left>
      <p class="text-gray-500 dark:text-gray-400 text-sm">
        Animal Food Bank © {{ new Date().getFullYear() }}.
      </p>
    </template>

    <template #right>
      <UColorModeButton size="sm" />
      <UButton to="https://github.com/AnimalFoodBank/afb-requests" target="_blank" icon="i-simple-icons-github" aria-label="GitHub" color="gray" variant="ghost" />
    </template>
  </UFooter>
</template>
