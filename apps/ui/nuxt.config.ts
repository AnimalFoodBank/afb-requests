// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  extends: [process.env.NUXT_UI_PRO_PATH || '@nuxt/ui-pro'],
  modules: [
    '@nuxt/ui',
    '@nuxt/fonts',
    'nuxt-snackbar',
    // '@storybook-vue/nuxt-storybook',
  ],

  /*
  *  Client-side Rendering:
  *  Out of the box, a traditional Vue.js application is rendered in the
  *  browser (or client). Then, Vue.js generates HTML elements after the
  *  browser downloads and parses all the JavaScript code containing the
  *  instructions to create the current interface. See:
  *  https://nuxt.com/docs/guide/concepts/rendering#client-side-rendering
  */
  ssr: false,

  ui: {
    icons: ['heroicons', 'streamline', 'ph', 'game-icons'], //
  },

  storybook: {
    url: 'http://localhost:6006',
    storybookRoute: '/__storybook__',
    port: 6006,
  },

  // 2024-02-02
  //
  // Used for success and error messages (e.g. after submitting
  // login form).
  snackbar: {
    // bottom: true,
    // right: true,
    duration: 10000,
  },

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

  // https://devtools.nuxt.com/guide/getting-started
  // enabled: process.env.NUXT_DEVTOOLS === 'true',
  devtools: {
    enabled: true,
    vscode: {
      startOnBoot: false,
      enabled: false,
      reuseExistingServer: true,
      port: 8118,  // code-server --port 8118
      mode: 'local-serve',  // 'tunnel' or 'local-serve',
      tunnel: {
        name: 'tundra',
        password: 'tundra',
      },
    },
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
