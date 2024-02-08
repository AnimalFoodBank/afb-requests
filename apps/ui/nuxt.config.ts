// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  extends: [process.env.NUXT_UI_PRO_PATH || '@nuxt/ui-pro'],
  modules: [
    '@nuxt/content',
    '@nuxt/image',
    '@nuxt/ui',
    '@nuxthq/studio',
    '@nuxtjs/fontaine',
    '@nuxtjs/google-fonts',
    '@vueuse/nuxt',
    "@pinia/nuxt",
    "@sidebase/nuxt-auth",
    'nuxt-og-image',
    'nuxt-snackbar',
  ],
  hooks: {
    // Define `@nuxt/ui` components as global to use them in `.md` (feel free to add those you need)
    'components:extend': (components) => {
      const globals = components.filter((c) => ['UButton'].includes(c.pascalName))

      globals.forEach((c) => c.global = true)
    }
  },
  ui: {
    icons: ['heroicons', 'simple-icons']
  },
  auth: {
    // This value is used for the auth origin. When it's not set, it'll raise
    // an AUTH_NO_ORIGIN error in production. In dev, it'll just log a warning.
    // @see https://github.com/sidebase/nuxt-auth/issues/515
    baseURL: process.env.NUXT_PUBLIC_APP_ORIGIN,

    // TODO: Check if this is still the right way to enable global middleware in Nuxt3
    // enableGlobalAppMiddleware: true,
  },
  // Fonts
  fontMetrics: {
    fonts: ['DM Sans']
  },
  googleFonts: {
    display: 'swap',
    download: true,
    families: {
      'DM+Sans': [300, 400, 500, 600, 700]
    }
  },
  snackbar: {
    // bottom: true,
    // right: true,
    duration: 10000,
  },
  routeRules: {
    '/api/search.json': { prerender: true },
    '/docs': { redirect: '/docs/getting-started', prerender: false }
  },
  devtools: {
    // https://devtools.nuxt.com/guide/getting-started
    enabled: process.env.NUXT_DEVTOOLS === 'true',
  },
  runtimeConfig: {
    AUTH_GOOGLE_CLIENT_SECRET: process.env.AUTH_GOOGLE_CLIENT_SECRET,

    APP_ORIGIN: process.env.NUXT_PUBLIC_APP_ORIGIN,
    AUTH_SECRET: process.env.AUTH_SECRET,  // TODO: Raise heck if not set

    // Public keys are exposed to the client
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || ':8000/',
      AUTH_GOOGLE_CLIENT_ID: process.env.AUTH_GOOGLE_CLIENT_ID
    },
  }
})
