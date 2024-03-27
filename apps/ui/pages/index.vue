
<script setup>
import { ref } from 'vue';

useSeoMeta({
  title: "AFB - Animal Food Bank",
  titleTemplate: '',
})

definePageMeta({
  auth: false,
});

const navigation = [
  { name: 'Product', href: '#' },
  { name: 'Features', href: '#' },
  { name: 'Marketplace', href: '#' },
  { name: 'Company', href: '#' },
]

const mobileMenuOpen = ref(false)
</script>

<template>
  <div class="relative bg-white dark:bg-slate-800">
    <div class="mx-auto max-w-7xl lg:grid lg:grid-cols-12 lg:gap-x-8 lg:px-8">
      <div class="px-6 pb-24 pt-10 sm:pb-32 lg:col-span-7 lg:px-0 lg:pb-56 lg:pt-48 xl:col-span-6">
        <div class="mx-auto max-w-2xl lg:mx-0">

          <div class="hidden sm:mt-32 sm:flex lg:mt-16">
            <!-- <div class="relative rounded-full px-3 py-1 text-sm leading-6 text-gray-500 ring-1 ring-gray-900/10 hover:ring-gray-900/20">
              Anim aute id magna aliqua ad ad non deserunt sunt. <a href="#" class="whitespace-nowrap font-semibold text-indigo-600"><span class="absolute inset-0" aria-hidden="true" />Read more <span aria-hidden="true">&rarr;</span></a>
            </div> -->
          </div>
          <h1 class="mt-24 text-4xl font-bold tracking-tight text-gray-900 dark:text-gray-200 sm:mt-10 sm:text-6xl">Animal Food Bank</h1>
          <p class="mt-6 text-lg leading-8 text-gray-600 dark:text-gray-200">
            Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo. Elit sunt amet fugiat veniam occaecat fugiat aliqua.
          </p>
          <div class="mt-10 flex items-center gap-x-6">
            <a href="/requests/new" class="rounded-md bg-black text-white dark:bg-white dark:text-black px-3.5 py-2.5 text-sm font-semibold shadow-sm">
              Request Pet Food
            </a>
            <a href="#" class="rounded-md text-sm font-semibold leading-6 bg-slate-100 text-gray-900 dark:bg-gray-900 dark:text-slate-100 px-3.5 py-2.5 ">Learn more <span aria-hidden="true">→</span></a>
          </div>
        </div>
      </div>
      <div class="relative lg:col-span-5 lg:-mr-8 xl:absolute xl:inset-0 xl:left-1/2 xl:mr-0">
        <img class="aspect-[3/2] w-full bg-gray-50 object-cover lg:absolute lg:inset-0 lg:aspect-auto lg:h-full" src="/img/about-7.jpg" alt="" />
      </div>
    </div>
  </div>
  <div class="absolute inset-x-0 top-[calc(100%-13rem)] -z-10 transform-gpu overflow-hidden blur-3xl sm:top-[calc(100%-30rem)]" aria-hidden="true">
    <div class="relative left-[calc(50%+3rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 bg-gradient-to-tr from-[#87e5ad] to-[#22a3ba] opacity-30 sm:left-[calc(50%+36rem)] sm:w-[72.1875rem]" style="clip-path: polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)" />
  </div>
</template>


<!--

title: 'Welcome - Animal Food Bank'
description: A non-profit organization dedicated to providing food supplies for animals in need.
navigation: false
hero:
  title: 'Animal Food Bank'
  description: 'A food bank for pets.'
  orientation: horizontal
  headline:
    label: ""
    to: https://animalfoodbank.org/#headline
    icon: i-heroicons-arrow-top-right-on-square-20-solid
  links:
    - label: Make a request
      icon: i-heroicons-arrow-right-20-solid
      trailing: true
      to: '/requests/new'
      size: lg
    - label: Learn about AFB
      icon: i-heroicons-building-storefront
      size: lg
      color: gray
      to: https://animalfoodbank.org/#learn-more
      target: _blank
about:
  title: 'About Us'
  description: 'We are a non-profit organization dedicated to providing food supplies for animals in need.'
  image: /images/hero.jpg
  orientation: horizontal
  links:
    - label: Learn more
      to: https://animalfoodbank.org/#about
      target: _blank
      icon: i-heroicons-arrow-right-20-solid
      size: lg
      color: gray
    - label: Make a request
      to: '/requests/new'
      icon: i-heroicons-arrow-right-20-solid
      size: lg
      color: gray
      trailing: true


 -->
