<template>
  <!--
    This example requires updating your template:

    ```
    <html class="h-full bg-gray-100">
    <body class="h-full">
      ```
    -->
    <div class="min-h-full">
      <div class="bg-indigo-600 pb-32">
        <Disclosure as="nav" class="border-b border-indigo-300 border-opacity-25 bg-indigo-600 lg:border-none"
        v-slot="{ open }">
        <div class="mx-auto max-w-7xl px-2 sm:px-4 lg:px-8">
          <div class="relative flex h-16 items-center justify-between lg:border-b lg:border-indigo-400 lg:border-opacity-25">

            <!-- Homepage link -->
            <div class="flex items-center px-2 lg:px-0">
              <div class="flex-shrink-0">
                <!--
                  Renders the company logo as an image.
                  The @ symbol in the src attribute is used to indicate that the path is relative to the project's src directory.
                -->
                <a href="/"><img class="block h-8 w-8" src="@/assets/img/afb_icon_colour.png" alt="Animal Food Bank logo" /></a>
              </div>

              <!-- Main navigation -->
              <div class="hidden lg:ml-10 lg:block">
                <nav class="pl-0 ml-0">
                  <div class="flex space-x-4 ">

                    <router-link v-for="item in navigation"
                    :key="item.name" :to="item.href" class="nav-link rounded-md py-2 px-3 text-sm font-medium text-white hover:bg-indigo-500 hover:bg-opacity-75">{{ item.name }}
                  </router-link>

                </div>
              </nav>
            </div>
          </div>

          <!-- Site search bar -->
          <div class="flex flex-1 justify-center px-2 lg:ml-6 lg:justify-end">
            <div class="w-full max-w-lg lg:max-w-xs">
              <label for="search" class="sr-only">Search</label>
              <div class="relative text-gray-400 focus-within:text-gray-600">
                <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3">
                  <MagnifyingGlassIcon class="h-5 w-5" aria-hidden="true" />
                </div>
                <input id="search"
                class="block w-full rounded-md border-0 bg-white py-1.5 pl-10 pr-3 text-gray-900 focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-600 sm:text-sm sm:leading-6"
                placeholder="Search" type="search" name="search" />
              </div>
            </div>
          </div>

          <!-- Mobile menu button -->
          <div class="flex lg:hidden">
            <DisclosureButton
            class="relative inline-flex items-center justify-center rounded-md bg-indigo-600 p-2 text-indigo-200 hover:bg-indigo-500 hover:bg-opacity-75 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-600">
            <span class="absolute -inset-0.5" />
            <span class="sr-only">Open main menu</span>
            <Bars3Icon v-if="!open" class="block h-6 w-6" aria-hidden="true" />
            <XMarkIcon v-else class="block h-6 w-6" aria-hidden="true" />
          </DisclosureButton>
        </div>

        <!-- Notifications bell -->
        <div class="hidden lg:ml-4 lg:block">
          <div class="flex items-center">
            <button type="button"
            class="relative flex-shrink-0 rounded-full bg-indigo-600 p-1 text-indigo-200 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-600">
            <span class="absolute -inset-1.5" />
            <span class="sr-only">View notifications</span>
            <BellIcon class="h-6 w-6" aria-hidden="true" />
          </button>

          <!-- Profile dropdown navigation (Desktop) -->
          <Menu as="div" class="relative ml-3 flex-shrink-0">
            <div>
              <MenuButton
              class="relative flex rounded-full bg-indigo-600 text-sm text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-600">
              <span class="absolute -inset-1.5" />
              <span class="sr-only">Open user menu</span>
              <img class="h-8 w-8 rounded-full" :src="user.imageUrl" alt="" />
            </MenuButton>
          </div>
          <transition enter-active-class="transition ease-out duration-100"
          enter-from-class="transform opacity-0 scale-95"
          enter-to-class="transform opacity-100 scale-100"
          leave-active-class="transition ease-in duration-75"
          leave-from-class="transform opacity-100 scale-100"
          leave-to-class="transform opacity-0 scale-95">
          <MenuItems
          class="absolute right-0 z-10 mt-2 w-48 origin-top-right rounded-md bg-white py-1 shadow-lg ring-1 ring-black ring-opacity-5 focus:outline-none">
          <MenuItem v-for="item in navigationItems" :key="item.name" v-slot="{ active }">
            <a
              :href="item.href"
              :class="[active ? 'bg-gray-100' : '', 'block px-4 py-2 text-sm text-gray-700']">{{ item.name
            }}</a>
          </MenuItem>
        </MenuItems>
      </transition>
    </Menu>
  </div>
</div>
</div>
</div>

<!-- Dropdown navigation (mobile) -->
<DisclosurePanel class="lg:hidden">
  <div class="space-y-1 px-2 pb-3 pt-2">
    <DisclosureButton v-for="item in navigationItems" :key="item.name" as="a" :href="item.href"
    :class="'block rounded-md py-2 px-3 text-base font-medium'"
    :aria-current="'page'">{{ item.name }}</DisclosureButton>
  </div>
  <div class="border-t border-indigo-700 pb-3 pt-4">
    <div class="flex items-center px-5">
      <div class="flex-shrink-0">
        <img class="h-10 w-10 rounded-full" :src="user.imageUrl" alt="" />
      </div>
      <div class="ml-3">
        <div class="text-base font-medium text-white">{{ user.name }}</div>
        <div class="text-sm font-medium text-indigo-300">{{ user.email }}</div>
      </div>
      <button type="button"
      class="relative ml-auto flex-shrink-0 rounded-full bg-indigo-600 p-1 text-indigo-200 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-indigo-600">
      <span class="absolute -inset-1.5" />
      <span class="sr-only">View notifications</span>
      <BellIcon class="h-6 w-6" aria-hidden="true" />
    </button>
  </div>
  <div class="mt-3 space-y-1 px-2">
    <DisclosureButton v-for="item in navigationItems" :key="item.name" as="a" :href="item.href"
    class="block rounded-md px-3 py-2 text-base font-medium text-white hover:bg-indigo-500 hover:bg-opacity-75">
    {{ item.name }}
  </DisclosureButton>
</div>
</div>
</DisclosurePanel>
</Disclosure>

</div>

<!-- Page content -->
<main class="-mt-32">
  <div class="mx-auto max-w-7xl px-4 pb-12 sm:px-6 lg:px-8">
    <div class="rounded-lg bg-white px-5 py-6 shadow sm:px-6">

      <slot></slot>

    </div>
  </div>
</main>

<!-- Footer -->
<footer class="mx-auto mt-40 max-w-7xl overflow-hidden px-6 pb-20 sm:mt-64 sm:pb-24 lg:px-8">
  <nav class="-mb-6 columns-2 sm:flex sm:justify-center sm:space-x-12" aria-label="Footer">
    <div v-for="item in footerNavigation.main" :key="item.name" class="pb-6">
      <a :href="item.href" class="text-sm leading-6 text-gray-600 hover:text-gray-900">{{ item.name }}</a>
    </div>
  </nav>
  <div class="mt-10 flex justify-center space-x-10">
    <a v-for="item in footerNavigation.social" :key="item.name" :href="item.href" class="text-gray-400 hover:text-gray-500">
      <span class="sr-only">{{ item.name }}</span>
      <component :is="item.icon" class="h-6 w-6" aria-hidden="true" />
    </a>
  </div>
  <p class="mt-10 text-center text-xs leading-5 text-gray-500">&copy; © 2023 Animal Food Bank / All Rights Reserved</p>
</footer>
</div>
</template>

<!-- NOTE: When setup is missing, the router/index.ts shows a warning that ApplicationPage isn't a module -->
<script setup lang="ts">
import CatHeartImage from '@/assets/img/Cat-Heart-680x800-1.png';
import { Disclosure, DisclosureButton, DisclosurePanel, Menu, MenuButton, MenuItem, MenuItems } from '@headlessui/vue';
import { MagnifyingGlassIcon } from '@heroicons/vue/20/solid';
import { Bars3Icon, BellIcon, XMarkIcon } from '@heroicons/vue/24/outline';
import axios from 'axios';
import { computed, defineComponent, h, onMounted, reactive, ref } from 'vue';
import { useAuthStore } from '../stores/auth';
const authStore = useAuthStore();

// Create an instance of axios to use in this module.
// See defaults set in /src/main.ts
const http_client = axios.create();

// Set the AUTH token for any request
http_client.interceptors.request.use(function (config) {
  if (authStore.isAuthenticated) {
    const token = authStore.getToken;
    console.log('http_client.interceptors.request.use()', token);
    config.headers.Authorization = token ? `Token ${token}` : '';
  }
  return config;
});

// Demonstrates how to use environment variables in Vue components.
console.log('import.meta.env.VITE_BASE_URL=' + import.meta.env.VITE_BASE_URL)

/**
* Makes a GET request to the current user endpoint and sets the user value if the response status is within the 200-299 range.
* If the response status is outside the 200-299 range, an error message is logged to the console.
* If there is a network error or the request is rejected, an error message is logged to the console.
* Note: axios automatically rejects the promise if the status code is outside the 200-299 range, so the else branch in this example might not be necessary depending on your axios configuration.
*/
onMounted(async () => {
  try {
    const response = await http_client.get('/api/users/current_user/');
    if (response.status >= 200 && response.status < 300) {
      user = reactive(Object.assign(user, response.data));
      user.is_authenticated = true;
      console.log('onMounted() user=', user);
    } else {
      // console.error(`Request failed with status code ${response.status}`);
      user = reactive(Object.assign(user, guestUser.value));
    }
  } catch (error) {
    // console.error('Request failed', error);
    user = reactive(Object.assign(user, guestUser.value));
  }
});

let user = reactive({
  is_admin: false,
  is_staff: false,
  is_authenticated: false,
  name: '',
  username: '',
  email: '',
  imageUrl: CatHeartImage,
});

let guestUser = ref({
  is_admin: false,
  is_staff: false,
  is_authenticated: false,
  name: 'Heart Cat',
  username: 'heartcat@animalfoodbank.org',
  email: '',
  imageUrl: CatHeartImage,
});

const navigation = [
{ name: 'Dashboard', href: '/dashboard'},
{ name: 'About', href: '/about'},
{ name: 'Requests', href: '/requests'},
]

const userNavigation = [
{ name: 'Your Profile', href: '/profile' },
{ name: 'Your dashboard', href: '/dashboard' },
{ name: 'Sign out', href: '/logout' },
]

const guestNavigation = [
{ name: 'Sign in', href: '/login' },
];

const navigationItems = computed(() => {
  console.log(user.is_authenticated)
  return user.is_authenticated ? userNavigation : guestNavigation;
});

const footerNavigation = {
  main: [
  { name: 'Blog', href: '#' },
  { name: 'About Us', href: '/about' },
  { name: 'Pet Food Recovery Program', href: 'https://animalfoodbank.org/afb-national-pet-food-recovery-program/' },
  { name: 'Get Help', href: 'https://animalfoodbank.org/get-help/' },
  { name: 'AFB Pet Club', href: 'https://afbpetclub.org' },
  { name: 'Sponsorship', href: 'https://animalfoodbank.org/sponsorship/' },
  ],
  social: [
  {
    name: 'Facebook',
    href: 'https://www.facebook.com/animalfoodbankcanada',
    icon: defineComponent({
      render: () =>
      h('svg', { fill: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', {
        'fill-rule': 'evenodd',
        d: 'M22 12c0-5.523-4.477-10-10-10S2 6.477 2 12c0 4.991 3.657 9.128 8.438 9.878v-6.987h-2.54V12h2.54V9.797c0-2.506 1.492-3.89 3.777-3.89 1.094 0 2.238.195 2.238.195v2.46h-1.26c-1.243 0-1.63.771-1.63 1.562V12h2.773l-.443 2.89h-2.33v6.988C18.343 21.128 22 16.991 22 12z',
        'clip-rule': 'evenodd',
      }),
      ]),
    }),
  },
  {
    name: 'Instagram',
    href: 'https://www.instagram.com/animalfoodbank/',
    icon: defineComponent({
      render: () =>
      h('svg', { fill: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', {
        'fill-rule': 'evenodd',
        d: 'M12.315 2c2.43 0 2.784.013 3.808.06 1.064.049 1.791.218 2.427.465a4.902 4.902 0 011.772 1.153 4.902 4.902 0 011.153 1.772c.247.636.416 1.363.465 2.427.048 1.067.06 1.407.06 4.123v.08c0 2.643-.012 2.987-.06 4.043-.049 1.064-.218 1.791-.465 2.427a4.902 4.902 0 01-1.153 1.772 4.902 4.902 0 01-1.772 1.153c-.636.247-1.363.416-2.427.465-1.067.048-1.407.06-4.123.06h-.08c-2.643 0-2.987-.012-4.043-.06-1.064-.049-1.791-.218-2.427-.465a4.902 4.902 0 01-1.772-1.153 4.902 4.902 0 01-1.153-1.772c-.247-.636-.416-1.363-.465-2.427-.047-1.024-.06-1.379-.06-3.808v-.63c0-2.43.013-2.784.06-3.808.049-1.064.218-1.791.465-2.427a4.902 4.902 0 011.153-1.772A4.902 4.902 0 015.45 2.525c.636-.247 1.363-.416 2.427-.465C8.901 2.013 9.256 2 11.685 2h.63zm-.081 1.802h-.468c-2.456 0-2.784.011-3.807.058-.975.045-1.504.207-1.857.344-.467.182-.8.398-1.15.748-.35.35-.566.683-.748 1.15-.137.353-.3.882-.344 1.857-.047 1.023-.058 1.351-.058 3.807v.468c0 2.456.011 2.784.058 3.807.045.975.207 1.504.344 1.857.182.466.399.8.748 1.15.35.35.683.566 1.15.748.353.137.882.3 1.857.344 1.054.048 1.37.058 4.041.058h.08c2.597 0 2.917-.01 3.96-.058.976-.045 1.505-.207 1.858-.344.466-.182.8-.398 1.15-.748.35-.35.566-.683.748-1.15.137-.353.3-.882.344-1.857.048-1.055.058-1.37.058-4.041v-.08c0-2.597-.01-2.917-.058-3.96-.045-.976-.207-1.505-.344-1.858a3.097 3.097 0 00-.748-1.15 3.098 3.098 0 00-1.15-.748c-.353-.137-.882-.3-1.857-.344-1.023-.047-1.351-.058-3.807-.058zM12 6.865a5.135 5.135 0 110 10.27 5.135 5.135 0 010-10.27zm0 1.802a3.333 3.333 0 100 6.666 3.333 3.333 0 000-6.666zm5.338-3.205a1.2 1.2 0 110 2.4 1.2 1.2 0 010-2.4z',
        'clip-rule': 'evenodd',
      }),
      ]),
    }),
  },
  {
    name: 'GitHub',
    href: 'https://github.com/AnimalFoodBank',
    icon: defineComponent({
      render: () =>
      h('svg', { fill: 'currentColor', viewBox: '0 0 24 24' }, [
      h('path', {
        'fill-rule': 'evenodd',
        d: 'M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z',
        'clip-rule': 'evenodd',
      }),
      ]),
    }),
  },
  ],
}
</script>



<style>

</style>
