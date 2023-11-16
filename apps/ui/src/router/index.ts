import {
  createRouter,
  createWebHistory,
  RouteMeta,
  RouteRecordRaw,
} from 'vue-router'

import ApplicationPage from '../layouts/ApplicationPage.vue'
import LoginPage from '../layouts/LoginPage.vue'

import MakeRequestView from '../views/MakeRequestView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import LoginView from '../views/LoginView.vue'


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


/**
 * The `privateApplicationRoute` constant is a metadata object that defines the properties for private application routes.
 *
 * @property {boolean} requiresAuth - A boolean value indicating whether the route requires authentication.
 * @property {Component} layout - The layout component to be used for the route.
 */
const privateApplicationRoute: RouteMeta = {
  requiresAuth: true,
  layout: ApplicationPage,
}

const publicApplicationRoute: RouteMeta = {
  requiresAuth: false,
  layout: ApplicationPage,
}

const publicLoginRoute: RouteMeta = {
  requiresAuth: false,
  layout: LoginPage,
}


const publicRoutes: Route[] = [
  {
      path: '/login',
      component: LoginView,
      name: 'LoginView',
      meta: publicLoginRoute,
  },
  {
      path: '/:pathMatch(.*)*',
      component: NotFoundView,
      name: 'NotFoundView',
      meta: publicLoginRoute,
  },
]

const applicationRoutes: Route[] = [
  {
    path: '/',
    component: DashboardView,
    name: 'DashboardView',  //  TODO: Rename to HomeView
    alias: '/dashboard',
    meta: privateApplicationRoute,
  },
  {
      path: '/requests',
      component: MakeRequestView,
      name: 'MakeRequestView',
      meta: privateApplicationRoute,
  },
  {
      path: '/about',
      component: AboutView,
      name: 'AboutView',
      children: [
        // https://router.vuejs.org/guide/essentials/nested-routes
      ],
      meta: privateApplicationRoute,
  },
]

const routes: RouteRecordRaw[] = (
  publicRoutes.concat(applicationRoutes) as RouteRecordRaw[]
)

const router = createRouter({
  history: createWebHistory(),
  routes  // TODO:
          // Type 'Route[]' is not assignable to type 'readonly RouteRecordRaw[]'.
          // Type 'Route' is not assignable to type 'RouteRecordRaw'.
})

// To ensure it is treated as a module,
// add at least one `export` statement
export default router
