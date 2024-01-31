// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  extends: [process.env.NUXT_UI_PRO_PATH || '@nuxt/ui-pro'],
  modules: [
    '@nuxt/content',
    '@nuxt/image',
    '@nuxt/ui',
    '@nuxthq/studio',
    '@nuxtjs/fontaine',
    '@nuxt/typescript-build',
    '@nuxtjs/google-fonts',
    '@vueuse/nuxt',
    'nuxt-og-image',
    "@pinia/nuxt"
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
  routeRules: {
    '/api/search.json': { prerender: true },
    '/docs': { redirect: '/docs/getting-started', prerender: false }
  },
  devtools: {
    // https://devtools.nuxt.com/guide/getting-started
    enabled: true
  },
  runtimeConfig: {
    // Will be available in both server and client
    mySecret: process.env.MY_SECRET,
    // Private keys are only available on the server
    apiSecret: '123',

    // Public keys that are exposed to the client
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || ':8000/'
    },
    // public: {
    //   baseURL: process.env.BASE_URL || ':8080/',
    // },
  },
  vite: {
    // Vite specific configuration
    // For example, to configure the server port:
    server: {
    },
    // Or to configure Rollup plugins:
    plugins: [
      // your plugins here
    ],
    // Or to configure resolve alias:
    resolve: {
      alias: {
        // your alias here
      }
    }
  }
})
