<script setup lang="ts">
import type { Button, FormError, FormEventType, FormGroupSize, FormSubmitEvent } from '#ui/types';
import { omit } from '#ui/utils';
import type { PropType } from 'vue';
import { useRoute } from 'vue-router';

const runtimeConfig = useRuntimeConfig();
const snackbar = useSnackbar();

definePageMeta({
  layout: 'auth',
  auth: {
    unauthenticatedOnly: true,
    navigateAuthenticatedTo: '/protected',
  },
})

const route = useRoute()
const email = route.query.email as string
const code = route.query.code as string

const fields = [{
  name: 'email',
  type: 'text',
  label: 'Email',
  placeholder: 'Enter your email',
  description: 'We will send you a magic link to sign in',
}]

// const state = reactive({
//   email,
//   code,
// })

// re: issues with autopopulating values and Chrome not updating the DOM
// see: https://github.com/vuejs/vue/issues/7058#issuecomment-1366489524
const validate = (state: any): FormError[] => {
  console.log('statevalidate', state)
  const errors = []
  if (!state.email) errors.push({ path: 'email', message: 'Required' })
  if (!state.code) errors.push({ path: 'code', message: 'Required' })
  return errors
}

async function onSubmit (event: FormSubmitEvent<any>) {
  // Do something with data
  console.log("event", event)

  // Prepare the payload
  const payload = {
    email: state.email,
    code: state.code,
  }
  console.log('Payload:', payload)

  // Send post request to the API endpoint using Nuxt 3 useFetch
  //
  // data - RefImpl, the response data. The value is null until
  //    the request is successful. “RefImpl is commonly a reference
  //    implementation used by Vue.js.”
  // pending - boolean, true if the request is still pending
  // error - ObjectRefImpl, when error.value is called, returns the error
  //    object or null. When null, the request was successful.
  // refresh - function, to manually trigger a new request.
  //
  // https://medium.com/@enestalayy/data-fetching-with-nuxt-3-ede89fb0509f
  //
  const path = '/api/passwordless/auth/token/'
  const { data, pending, error, refresh } = useFetch(path, {
    baseURL: runtimeConfig.public.apiBase,
    method: 'POST',
    body: JSON.stringify(payload),
    headers: {
      'Content-Type': 'application/json'
    },
    mode: 'cors',
  })

  // ObjectRefImpl is implemented by the Vue.js reactivity system.
  // https://github.com/vuejs/core/blob/75e02b5099a0/packages/reactivity/src/ref.ts#L357
  if (error.value) {
    console.error('An error occurred:', error)
    let response = event
    if (response.statusCode === 400) {
      const message = "Invalid email or code"
      console.log('Message:', message)

      snackbar.add({
        type: 'error',
        text: message,
      })
    }
    return
  }

  // A successful repsonse returns a friendly message for the
  // user. The next step is for the user to check their email
  // for the magic link to sign in.
  if (await data.value) {
    const response = (data.value);
    const message = "Thanks for that"
    console.log('Message:', message)

    snackbar.add({
      type: 'success',
      text: message,
    })
  }

}

/**
 * UI classes
 */


const config = {
  wrapper: 'w-full max-w-sm space-y-6',
  base: '',
  container: 'gap-y-6 flex flex-col',
  title: 'text-2xl text-gray-900 dark:text-white font-bold',
  description: 'text-gray-500 dark:text-gray-400 mt-1',
  icon: {
    wrapper: 'mb-2 pointer-events-none',
    base: 'w-8 h-8 flex-shrink-0 text-gray-900 dark:text-white'
  },
  providers: 'space-y-3',
  form: 'space-y-6',
  footer: 'text-sm text-gray-500 dark:text-gray-400 mt-2',
  default: {
    submitButton: {
      label: 'Continue'
    }
  }
}

defineOptions({
  inheritAttrs: false
})

const props = defineProps({
  title: {
    type: String,
    default: undefined
  },
  description: {
    type: String,
    default: undefined
  },
  icon: {
    type: String,
    default: undefined
  },
  align: {
    type: String as PropType<'top' | 'bottom'>,
    default: 'bottom'
  },
  loading: {
    type: Boolean,
    default: false
  },
  fields: {
    type: Array as PropType<{
      name: string
      type: string
      label: string
      description?: string
      help?: string
      hint?: string
      size?: FormGroupSize
      placeholder?: string
      required?: boolean
    }[]>,
    default: () => []
  },
  providers: {
    type: Array as PropType<(Button & { click?: Function })[]>,
    default: () => []
  },
  submitButton: {
    type: Object as PropType<Button>,
    default: () => ({})
  },
  schema: {
    type: Object as PropType<any>,
    default: undefined
  },
  validate: {
    type: [Function, Array] as PropType<((state: any) => Promise<FormError[]>) | ((state: any) => FormError[])>,
    default: undefined
  },
  validateOn: {
    type: Array as PropType<FormEventType[]>,
    default: () => ['submit']
  },
  divider: {
    type: String,
    default: 'or'
  },
  class: {
    type: [String, Object, Array] as PropType<any>,
    default: undefined
  },
  ui: {
    type: Object as PropType<Partial<typeof config>>,
    default: () => ({})
  }
})

defineEmits(['submit'])

const formRef = ref<HTMLElement>()

const { ui, attrs } = useUI('auth.form', toRef(props, 'ui'), config, toRef(props, 'class'), true)

const state = reactive(Object.values(props.fields).reduce((acc, { name }) => {
  acc[name] = undefined
  return acc
}, {} as Record<string, any>))

// Expose

defineExpose({
  formRef
})

</script>

<template>
  <UCard class="max-w-sm w-full bg-white/75 dark:bg-white/5 backdrop-blur">
    <img src="/img/afb_icon_black.png" alt="Logo" class="mx-auto w-24 h-24 rounded-full" />

    <!-- https://ui.nuxt.com/components/form -->
    <!-- https://ui.nuxt.com/pro/components/auth-form -->
          <UForm
          ref="formRef"
          :state="state"
          :schema="schema"
          :validate="validate"
          :validate-on="validateOn"
          :class="ui.form"
          @submit="$emit('submit', $event.data)"
        >
          <UFormGroup
            v-for="field in fields"
            :key="field.name"
            :label="field.label"
            :description="field.description"
            :help="field.help"
            :hint="field.hint"
            :name="field.name"
            :size="field.size"
          >
            <UInput v-model="state[field.name]" v-bind="omit(field, ['label', 'description', 'help', 'hint', 'size'])" />

            <template v-if="$slots[`${field.name}-label`]" #label>
              <slot :name="`${field.name}-label`" />
            </template>
            <template v-if="$slots[`${field.name}-description`]" #description>
              <slot :name="`${field.name}-description`">
                <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">{{ field.description }}</p>
              </slot>
            </template>
            <template v-if="$slots[`${field.name}-hint`]" #hint>
              <slot :name="`${field.name}-hint`" />
            </template>
            <template v-if="$slots[`${field.name}-help`]" #help>
              <slot :name="`${field.name}-help`" />
            </template>
          </UFormGroup>

          <UButton type="submit" block :loading="loading" v-bind="{ ...ui.default.submitButton, ...submitButton }" />
        </UForm>
  </UCard>
</template>
