// via https://blog.logrocket.com/how-use-axios-vue-js/

import axios from 'axios'
import type {App} from 'vue'

interface AxiosOptions {
  baseURL?: string
  token?: string
}

export default {
  install: (app: App, options: AxiosOptions) => {
    app.config.globalProperties.$axios = axios.create({
      baseURL: options.baseURL,
      headers: {
        Authorization: options.token ? `Bearer ${options.token}` : '',
      }
    })
  }
}
