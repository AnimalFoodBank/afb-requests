import {defineStore} from 'pinia'

export const settingsStore = defineStore('settings', {
  state: () => ({
    language: '',
    theme: 'light',
    preference_theme: 'auto',
    environment: {
      id: 0,
      name: 'Local'
    }
  }),
  getters: {
    is_remote(): boolean {
      return this.environment.id !== 0
    }
  },
  actions: {
    set_language(lang: string) {
      this.language = lang
    },
    set_theme(t: string) {
      this.theme = t
    },
    clear_environment() {
      this.environment.id = 0
      this.environment.name = 'Local'
    }
  },
  persist: true
})
