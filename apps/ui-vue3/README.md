# AFB UI

## Commands
https://vitejs.dev/guide/cli.html

- **template of:** vite + vue + typescript
- **tailwindcss:** v3.x

### Started

```bash
pnpm install --shamefully-hoist
# or `yarn`
# or `npm install`
```

### Develop

```bash
pnpm run dev
# or `yarn dev`
# or `npm run dev`
```

### Build

```bash
pnpm run build
# yarn build
# or `npm run build`
```

---


## About Vue apps

In a Vite + Vue application, main.ts and index.ts have different roles:

main.ts: This is the entry point of your Vue application. It's where you create the Vue instance and mount it to a DOM element. It's also where you import your root component, any global styles, plugins, and other global configurations.

index.ts: This file is typically used for organizing exports from a directory. In the context of Vue Router, index.ts is often used to define and export the router instance, as shown in your code snippet.

Here's a simplified example of how these files might be used:

```ts
// router/index.ts
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
```

In the main.ts file, we import the router from router/index.ts and use it in our Vue application.
