// https://nuxt.com/docs/api/configuration/nuxt-config

// https://nuxt.com/docs/api/configuration/nuxt-config
import type { SessionData } from "./types/index.d";

export default defineNuxtConfig({
  extends: [process.env.NUXT_UI_PRO_PATH || "@nuxt/ui-pro"],
  modules: [
    "@nuxt/ui",
    '@nuxt/test-utils/module',
    "@nuxt/fonts",
    "nuxt-snackbar",
    "@sidebase/nuxt-auth",
    "@vueform/nuxt",
    // '@vueform/builder-nuxt',
  ],

  build: {
    // transpile: ["@fawmi/vue-google-maps"],
  },

  /*
   *  Client-side Rendering:
   *  Set to false to disable client-side rendering.
   *
   *  Out of the box, a traditional Vue.js application is rendered in the
   *  browser (or client). Then, Vue.js generates HTML elements after the
   *  browser downloads and parses all the JavaScript code containing the
   *  instructions to create the current interface. See:
   *  https://nuxt.com/docs/guide/concepts/rendering#client-side-rendering
   */
  ssr: false,

  // nitro: {
  //   routeRules: {
  //     "/**/*.ts": {
  //       headers: {
  //         "content-type": "application/typescript",
  //       },
  //     },
  //     "/**/*.vue": {
  //       headers: {
  //         "content-type": "text/vue",
  //       },
  //     },
  //   },
  // },

  ui: {
    icons: ["heroicons", "streamline", "ph", "game-icons"], // simple-icons
  },

  //
  // https://sidebase.io/nuxt-auth/getting-started/quick-start#provider-refresh
  //
  // https://sidebase.io/nuxt-auth/application-side/session-access-and-management
  //
  //  - Local provider: Note that you will have to manually call getSession from
  //  useAuth composable in order to refresh the new user state when using
  //  setToken, clearToken or manually updating rawToken.value:
  //
  // https://sidebase.io/nuxt-auth/application-side/protecting-pages
  // https://sidebase.io/nuxt-auth/application-side/guest-mode
  //
  //
  // JS API Docs
  // https://github.com/sidebase/nuxt-auth/blob/5d713aa419/src/runtime/composables/authjs/useAuth.ts#L222
  // https://github.com/sidebase/nuxt-auth/blob/5d713aa419/docs/content/2.configuration/2.nuxt-config.md?plain=1#L176
  //
  auth: {
    isEnabled: true,
    globalAppMiddleware: true,
    baseURL: "/api/v1",
    provider: {
      type: "local",
      endpoints: {
        signIn: { path: "/passwordless/auth/token/", method: "post" },
        signOut: { path: "/authtoken/logout/", method: "post" },
        signUp: { path: "/register", method: "post" },
        getSession: { path: "/users/current_user/", method: "get" },
      },
      sessionDataType: {
        id: "string",
        email: "string",
        name: "string",
        role: "admin | guest | client | volunteer | branchmanager",
        subscriptions: "{ id: number, status: 'ACTIVE' | 'INACTIVE' }[]",
      },
      token: {
        signInResponseTokenPointer: "/token", // json path in response
        // type - one of 'Bearer' or 'Token'. The former is JWT, latter is TokenAuthentication)
        type: "Token",
        cookieName: 'auth.token',
        headerName: 'Authorization',
        maxAgeInSeconds: 3600 * 24 * 30,
        sameSiteAttribute: 'strict',
      },
    },
    session: {
      // Whether to refresh the session every time the browser window is refocused.
      enableRefreshOnWindowFocus: true,

      // Whether to refresh the session every `X` milliseconds. Set this to `false` to turn it off. The session will only be refreshed if a session already exists.
      enableRefreshPeriodically: 60000
    },
  },

  // storybook: {
  //   url: "http://localhost:6006",
  //   storybookRoute: "/__storybook__",
  //   port: 6006,
  // },

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
    // externalVue: false,
    // appManifest: false,
  },

  // https://devtools.nuxt.com/guide/getting-started
  // enabled: process.env.NUXT_DEVTOOLS === 'true',
  devtools: {
    enabled: true,
    vscode: {
      startOnBoot: false,
      enabled: false,
      reuseExistingServer: true,
      port: 8118, // code-server --port 8118
      mode: "local-serve", // 'tunnel' or 'local-serve',
      tunnel: {
        name: "tundra",
        password: "tundra",
      },
    },
    timeline: {
      enabled: true,
    },
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
    // Public keys are exposed to the client
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE,
      AUTH_GOOGLE_CLIENT_ID: process.env.AUTH_GOOGLE_CLIENT_ID,
    },
  },
});
