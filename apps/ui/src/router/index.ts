import {
  createRouter,
  createWebHistory,
  RouteMeta,
} from 'vue-router'

import ApplicationPage from '../layouts/ApplicationPage.vue'
import LoginPage from '../layouts/LoginPage.vue'

import MakeRequestView from '../views/MakeRequestView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import LoginView from '../views/LoginView.vue'


// TODO: Revisit lazy-loading suggestion from ? (component as a function that returns AboutVue)
// import AboutView from '../views/AboutView.vue';



// This can be directly added to any of your `.ts` files like `router.ts`
// It can also be added to a `.d.ts` file. Make sure it's included in
// project's tsconfig.json "files"

declare module 'vue-router' {
  // https://router.vuejs.org/api/interfaces/RouteMeta.html
  interface RouteMeta {
    // is optional
    isAdmin?: boolean
    // must be declared by every route
    requiresAuth?: boolean
    // Layout component to use
    layout: any
  }
}

type Route = {
  // Note: Route is not a type in vue-router
  // https://router.vuejs.org/api/#type-routes
  path: string;
  name: string;
  component: any;
  meta: RouteMeta;
  alias?: string;
  children?: Route[];
}

const defaultRoute: Route = {
  path: '/',
  component: DashboardView,
  name: 'DashboardView',  //  TODO: Rename to HomeView
  alias: '/dashboard',
  meta: { layout: 'ApplicationPage' },
};

const routes: Route[] = [
  defaultRoute,
  {
      path: '/requests',
      component: MakeRequestView,
      name: 'MakeRequestView',
      meta: { layout: ApplicationPage },
  },
  {
      path: '/about',
      component: AboutView,
      name: 'AboutView',
      children: [
        // https://router.vuejs.org/guide/essentials/nested-routes
      ],
      meta: { layout: ApplicationPage },
  },
  {
      path: '/login',
      component: LoginView,
      name: 'LoginView',
      meta: { layout: LoginPage },
  },
  {
      path: '/:pathMatch(.*)*',
      component: NotFoundView,
      name: 'NotFoundView',
      meta: { layout: ApplicationPage },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes  // TODO:
          // Type 'Route[]' is not assignable to type 'readonly RouteRecordRaw[]'.
          // Type 'Route' is not assignable to type 'RouteRecordRaw'.
})

// To ensure it is treated as a module,
// add at least one `export` statement
export default router
