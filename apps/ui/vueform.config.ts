// vueform.config.(js|ts)

import en from '@vueform/vueform/locales/en'
import tailwind from '@vueform/vueform/dist/tailwind'
import { defineConfig } from '@vueform/vueform'

import vueform from '@vueform/vueform/themes/vueform'
// import builder from '@vueform/builder/plugin'
import PluginMask from '@vueform/plugin-mask'

import axios from 'axios'
import type { AxiosRequestConfig } from 'axios';


const httpClient = axios.create({
  baseURL: '',
  withCredentials: true,
  onUnauthenticated() {
    location.href = '/login'
  },
})

httpClient.interceptors.request.use((config: AxiosRequestConfig) => {
  config.headers.AFBRules = "true"
  return config;
});

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
  addClasses: {
    Vueform: {
      form: 'afbcore-form',
    },
  },
  axios: httpClient,
})
