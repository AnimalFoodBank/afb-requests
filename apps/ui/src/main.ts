// add the beginning of your app entry
import 'vite/modulepreload-polyfill'

import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
import axios from 'axios'
import { createPinia } from 'pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'

// No need to load via a plugin. Just use it directly and use vite
// env variables to set the base url.
// https://stackoverflow.com/questions/77041139/using-axios-instance-in-vue-3
// import axios from './plugins/axios'

// import Vueform from '@vueform/vueform'
// import vueformConfig from './../vueform.config'
// import { Plugin } from 'vue'

const base_url = import.meta.env.VITE_BASE_URL;
axios.defaults.baseURL = base_url;

const app = createApp(App)
app.use(router)

// Use pinia for local state management. It's available
// on all components via this.$pinia.
// See https://prazdevs.github.io/pinia-plugin-persistedstate/guide/#usage
const pinia = createPinia()
pinia.use(piniaPluginPersistedstate)
app.use(pinia)

app.mount('#app')
