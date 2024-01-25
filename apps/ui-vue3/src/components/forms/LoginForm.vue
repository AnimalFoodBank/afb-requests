<!-- ./components/forms/LoginForm.vue -->

<!--
  re: VueForm in TS
  https://vuejs.org/guide/typescript/overview.html#configuring-tsconfig-json
  https://vuejs.org/guide/typescript/composition-api.html

  re: <script setup>
  https://vuejs.org/guide/typescript/overview.html#usage-in-single-file-components

  re: Hot reloads when using <LoginForm> in LoginView.vue,
    `npx vite` needs to be wholly restarted for some reason.

  *** NOTE: Not currently used b/c of the hot reloads issue. Edits the form in LoginForm.vue instead. ***
-->

<template>
  <form>
    <div class="w-full">
      <div class="w-full">
        <TextElement name="email" label="Email" />
      </div>
      <div class="w-full">
        <TextElement name="password" label="Password" />
      </div>
    </div>
  </form>
</template>

<script lang="ts">
/**
 * `useVueform` is a Composition API function
 * that should be called inside the setup function,
 * not used as the setup function itself. Also note
 * that the `vueform` object is a ref, so it needs
 * to be unwrapped when used in the template.
 */
import { Vueform, useVueform } from '@vueform/vueform';

export default {
  mixins: [Vueform],
  setup: useVueform,
  data: () => ({
    vueform: {
      schema: {
        email: { type: 'text', label: 'Email' },
        password: { type: 'password', inputType: 'password', label: 'Password' },
      }
    }
  })
}
</script>
