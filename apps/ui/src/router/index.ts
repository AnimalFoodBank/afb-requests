import {
  createRouter,
  createWebHistory
} from 'vue-router'
import MakeRequestView from '../views/MakeRequestView.vue'
import AboutView from '../views/AboutView.vue'
import DashboardView from '../views/DashboardView.vue'
import NotFoundView from '../views/NotFoundView.vue'

// TODO: Revisit lazy-loading suggestion from ? (component as a function that returns AboutVue)
// import AboutView from '../views/AboutView.vue';


type Route = {
  path: string;
  name: string;
  component: any;
}


const routes: Route[] = [
    {
      path: '/dashboard',
      component: DashboardView,
      name: 'DashboardView',
  },
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
