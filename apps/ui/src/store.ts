import { defineStore } from 'pinia';

export const useStore = defineStore({
  id: 'main',
  state: () => ({
    count: 0,
    name: 'Alice',
  }),
  getters: {
    double: (state) => state.count * 2,
    greeting: (state) => `Hello, ${state.name}!`,
  },
  actions: {
    increment() {
      this.count++
    },
  },
});
