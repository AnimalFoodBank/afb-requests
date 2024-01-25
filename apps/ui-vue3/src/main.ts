// add the beginning of your app entry
import 'vite/modulepreload-polyfill'

import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
import axios from 'axios'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

import Vueform from '@vueform/vueform'
import vueformConfig from './../vueform.config'

const base_url = import.meta.env.VITE_BASE_URL;

// https://stackoverflow.com/questions/68256028/forbidden-csrf-cookie-not-set-when-sending-post-delete-request-from-vue-js-to
// https://docs.djangoproject.com/en/dev/howto/csrf/#acquiring-csrf-token-from-html
//
// See also: vueform.config.ts
// https://vueform.com/reference/configuration#axios
axios.defaults.baseURL = base_url;
axios.defaults.withCredentials = true

// New as of 1.6.2: https://github.com/axios/axios/releases/tag/v1.6.2
axios.defaults.withXSRFToken = true

const app = createApp(App)
app.use(router)

// Use pinia for local state management. It's available
// on all components via this.$pinia.
// See https://prazdevs.github.io/pinia-plugin-persistedstate/guide/#usage
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)

app.use(Vueform, vueformConfig);


app.mount('#app')
