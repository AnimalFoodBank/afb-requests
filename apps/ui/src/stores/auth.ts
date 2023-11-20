import { defineStore } from 'pinia'
import { type Ref, ref, reactive } from "vue";


export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null as string | null,
    returnUrl: null as string | null,
    userDetails: null as any,
  }),
  getters: {
    isAuthenticated: (state) => !!state.token,
    getToken: (state) => state.token,
  },
  actions: {
    login(token: string) {
      this.token = token
    },
    logout() {
      this.token = null
    },
  },
  persist: true
})

// The userEmail is meant for keeping email state across auth pages, for example when going from login to forgot-password page
const userEmail = ref(null) as Ref<string | null>;
