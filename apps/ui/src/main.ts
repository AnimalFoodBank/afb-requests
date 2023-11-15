// add the beginning of your app entry
import 'vite/modulepreload-polyfill'

import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
import axios from 'axios'
// import { createPinia } from 'pinia'

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


// app.use(createPinia())
app.use(router)

// Assign the axios instance to a property in your Vue app's global properties
// app.config.globalProperties.$axios = axiosInstance


// Attach Vueform and its config
// app.use(Vueform as any, vueformConfig)

app.mount('#app')
