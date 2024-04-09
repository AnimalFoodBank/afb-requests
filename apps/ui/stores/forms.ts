import { defineStore } from 'pinia'

export const useFormsStore = defineStore('forms', {
  state: () => {
    return {
      foodrequestform: {}
    }
  },
})
