import {defineStore} from 'pinia'

export const authStore = defineStore('auth', {
  state: () => ({
    token: ''
  }),
  getters: {
    is_authenticated(state): boolean {
      return !!state.token
    }
  },
  actions: {
    login(token: string) {
      this.token = token
    },
    logout() {
      this.token = ''
    },
  },
  persist: true
})
