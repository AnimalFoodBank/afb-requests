import {
  createRouter,
  createWebHistory,
  RouteMeta,
  RouteRecordRaw,
} from 'vue-router'

import { useAuthStore } from '../stores/auth'

import ApplicationPage from '../layouts/ApplicationPage.vue'
import LoginPage from '../layouts/LoginPage.vue'

import MakeRequestView from '../views/MakeRequestView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import LoginView from '../views/LoginView.vue'
import LogoutView from '../views/LogoutView.vue'
import RegisterView from '../views/RegisterView.vue'
import HomePageView from '../views/HomePageView.vue'

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
    path: '/logout',
    component: LogoutView,
    name: 'LogoutView',
    meta: privateApplicationRoute,
  },
  {
    path: '/about',
    component: AboutView,
    name: 'AboutView',
    children: [
      // https://router.vuejs.org/guide/essentials/nested-routes
    ],
    meta: publicApplicationRoute,
  },
  {
    path: '/',
    component: HomePageView,
    name: 'HomePageView',
    meta: publicApplicationRoute,
  },
  {
    path: '/register',
    component: RegisterView,
    name: 'RegisterView',
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
    path: '/dashboard',
    component: DashboardView,
    name: 'DashboardView',  //  TODO: Rename to HomeView
    meta: privateApplicationRoute,
  },
  {
    path: '/requests',
    component: MakeRequestView,
    name: 'MakeRequestView',
    meta: privateApplicationRoute,
  },
]

const routes: RouteRecordRaw[] = (
  publicRoutes.concat(applicationRoutes) as RouteRecordRaw[]
  )

  const router = createRouter({
    history: createWebHistory(),
    routes
  })

  router.beforeEach(async (to) => {
    // redirect to login page if not logged in and trying to access a restricted page
    const authRequired = to.meta.requiresAuth;
    const auth = useAuthStore();

    if (authRequired && !auth.token) {
      auth.returnUrl = to.fullPath;
      return '/login';
    }
  });

  // To ensure it is treated as a module,
  // add at least one `export` statement
  export default router
