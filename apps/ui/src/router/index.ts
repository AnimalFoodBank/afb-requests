import {
  createRouter,
  createWebHistory
} from 'vue-router'
import MakeRequestView from '../views/MakeRequestView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import NotFoundView from '../views/NotFoundView.vue'
import LoginView from '../views/LoginView.vue'

// TODO: Revisit lazy-loading suggestion from ? (component as a function that returns AboutVue)
// import AboutView from '../views/AboutView.vue';


type Route = {
  path: string;
  name: string;
  component: any;
  alias?: string;
}


const defaultRoute: Route = {
  path: '/',
  component: DashboardView,
  name: 'DashboardView',
  alias: '/dashboard',
};

const routes: Route[] = [
  defaultRoute,
  {
      path: '/requests',
      component: MakeRequestView,
      name: 'MakeRequestView',
  },
  {
      path: '/about',
      component: AboutView,
      name: 'AboutView',
  },
  {
      path: '/login',
      component: LoginView,
      name: 'LoginView',
  },
  {
      path: '/:pathMatch(.*)*',
      component: NotFoundView,
      name: 'NotFoundView'
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
