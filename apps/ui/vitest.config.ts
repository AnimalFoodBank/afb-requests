// vitest.config.ts
import { fileURLToPath } from 'node:url'
import { defineVitestConfig } from '@nuxt/test-utils/config'

export default defineVitestConfig({
  // Via https://www.youtube.com/watch?v=yGzwk9xi9gU&list=PL06MUQt-_wlsRNxmbIvgVuhsXG_dN1XaO&index=28
  //
  // "The best way to test a Nuxt app is to use the
  // nuxt/test-utils package. It provides an API for testing
  // your application in different environments, such as
  // Node.js, JSDOM, or Nuxt itself. It also provides a way
  // to test your application in the browser, using Cypress
  // or Playwright."
  //
  // "The nuxt/test-utils package is built on top of the
  // popular Jest testing framework and uses Puppeteer for
  // running tests in Chromium."
  //
  test: {
    environment: 'nuxt',
    environmentOptions: {
      nuxt: {
        mock: {
          intersectionObserver: true,
          indexedDb: true,
        }
      }
    }
    // you can optionally set Nuxt-specific environment options
    // environmentOptions: {
    //   nuxt: {
    //     rootDir: fileURLToPath(new URL('./playground', import.meta.url)),
    //     domEnvironment: 'happy-dom', // 'happy-dom' (default) or 'jsdom'
    //     overrides: {
    //       // other Nuxt config you want to pass
    //     }
    //   }
    // }
  }

})
