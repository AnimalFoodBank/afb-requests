// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  extends: [process.env.NUXT_UI_PRO_PATH || '@nuxt/ui-pro'],
  modules: [
    '@nuxtjs/color-mode',
    '@nuxt/image',
    '@nuxt/ui',
    '@nuxthq/studio',  // https://nuxt.studio/docs/projects/setup#requirements-to-use-the-studio-editor
    '@nuxtjs/fontaine',
    '@nuxtjs/google-fonts',
    '@vueuse/nuxt',
    "@pinia/nuxt",
    // "@sidebase/nuxt-auth",
    'nuxt-og-image',
    'nuxt-snackbar',
  ],
  /*
    Client-side Rendering:
    Out of the box, a traditional Vue.js application is rendered in the
    browser (or client). Then, Vue.js generates HTML elements after the
    browser downloads and parses all the JavaScript code containing the
    instructions to create the current interface. See:
    https://nuxt.com/docs/guide/concepts/rendering#client-side-rendering
  */
  // ssr: false,

  // force module initialization on dev env
  // https://nuxt.studio/docs/developers/local-debug
  studio: {
    enabled: true
  },
  colorMode: {
    preference: 'dark', // default value of $colorMode.preference
    fallback: 'dark', // fallback value if not system preference found
    classSuffix: '',
    storageKey: 'nuxt-color-mode',
  },
  hooks: {
    // Define `@nuxt/ui` components as global to use them in `.md` (feel free to add those you need)
    'components:extend': (components) => {
      const globals = components.filter((c) => ['UButton'].includes(c.pascalName))

      globals.forEach((c) => c.global = true)
    }
  },
  ui: {
    icons: ['heroicons', 'simple-icons'],  // 'phosphor', 'streamline'
  },
  srcDir: '.', // This is the default, but it's good to be explicit
  // 2024-02-28
  //
  // re: "Cannot find module ... vue/server-renderer/index.mjs" when running nuxi
  // build and then "node .output/server/index.mjs"
  //
  // https://github.com/nuxt/nuxt/issues/14820#issuecomment-1890360196
  //
  experimental: {
    externalVue: false,
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
    // '/_api/search.json': { prerender: true },
    // '/docs': { redirect: '/docs/getting-started', prerender: false }
  },
  devtools: {
    // https://devtools.nuxt.com/guide/getting-started
    // enabled: process.env.NUXT_DEVTOOLS === 'true',
    enabled: true,

    timeline: {
      enabled: true
    }
  },
  /*
  * runtimeConfig is a configuration option that allows you to pass
  * environment variables from the server to the client. It has two
  * properties: publicRuntimeConfig and privateRuntimeConfig.
  *
  * runtimeConfig.public is the Nuxt 3 syntax for publicRuntimeConfig
  *
  * NOTE: The from server to client part is important. This means that
  * the client can access these variables, so be careful not to expose
  * sensitive information.
  */
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
