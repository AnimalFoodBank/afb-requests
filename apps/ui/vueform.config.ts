// vueform.config.(js|ts)

import en from '@vueform/vueform/locales/en'
import vueform from '@vueform/vueform/themes/vueform'
import tailwind from '@vueform/vueform/dist/tailwind'
import { defineConfig } from '@vueform/vueform'
// import builder from '@vueform/builder/plugin'
import PluginMask from '@vueform/plugin-mask'

export default defineConfig({
  theme: tailwind,
  locales: { en },
  locale: 'en',
  apiKey: 'sppy-spc3-valx-p0vf-sej6',
  endpoints: {
  },
  plugins: [
    // builder,
    PluginMask,
  ],
  // services: {
  //   google2: {
  //     app_id: '338793354229-r38ovlt05ltulgdf2ar6kcg5fhcg2ut3.apps.googleusercontent.com',
  //     project_id: '338793354229-r38ovlt05ltulgdf2ar6kcg5fhcg2ut3.apps.googleusercontent.com',
  //     api_key: 'AIzaSyC_UvqrTnimc1Pc7LDYCqdqUiGMMUgMCWg',
  //   }
  // }
})
