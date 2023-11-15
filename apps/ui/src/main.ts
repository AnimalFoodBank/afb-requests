// add the beginning of your app entry
import 'vite/modulepreload-polyfill'

import { createApp } from 'vue'
import App from './App.vue'
import './index.css'
import router from './router'
import axios from './plugins/axios'
import { createPinia } from 'pinia'

// import Vueform from '@vueform/vueform'
// import vueformConfig from './../vueform.config'
import { Plugin } from 'vue'


const app = createApp(App)

// app.use(createPinia())

app.use(router)

// app.use(axios, {
//   baseUrl: 'http://127.0.0.1:3000/',
// })

// Attach Vueform and its config
// app.use(Vueform as any, vueformConfig)

app.mount('#app')
