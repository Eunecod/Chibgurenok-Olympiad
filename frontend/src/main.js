import { createRouter, createWebHistory } from 'vue-router';
import { createApp }    from 'vue';
import { createPinia }  from 'pinia';

import _axios from '@/util/axioshandler.js';
import piniaPluginPersistedstate  from 'pinia-plugin-persistedstate';

import App      from '@/App.vue';
import Olympiad from '@/pages/Olympiad.vue';
import Profile  from '@/pages/Profile.vue';
import Contact  from '@/pages/Contact.vue';
import Signup   from '@/pages/Signup.vue';
import Result   from '@/pages/Result.vue';
import Login    from '@/pages/Login.vue';
import Rules    from '@/pages/Rules.vue';
import Quiz     from '@/pages/Quiz.vue';
import Main     from '@/pages/Main.vue';

import OlympiadAdmin  from '@/pages/Admin/OlympiadAdmin.vue';
import ResultAdmin    from '@/pages/Admin/ResultAdmin.vue';
import ReplyAdmin     from '@/pages/Admin/ReplyAdmin.vue';
import SignupAdmin    from '@/pages/Admin/SignupAdmin.vue';

import NotFound from '@/pages/Code/NotFound.vue';

import 'bulma/css/bulma.css';
//import '@/assets/fontawesome/css/all.min.css';

import ToastPlugin    from '@/plugin/toast.js';


const routes = [
  {
    path: '/',
    name: 'Main',
    component: Main,
    meta: { protected: false, admin: false }
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: { protected: false, admin: false }
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
    meta: { protected: false, admin: false }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
    meta: { protected: true, admin: false }
  },
  {
    path: '/quiz/:id',
    name: 'Quiz',
    component: Quiz,
    meta: { protected: true, admin: false },
    props: true
  },
  {
    path: '/result',
    name: 'Result',
    component: Result,
    meta: { protected: false, admin: false }
  },
  {
    path: '/rules',
    name: 'Rules',
    component: Rules,
    meta: { protected: false, admin: false }
  },
  {
    path: '/olympiad',
    name: 'Olympiad',
    component: Olympiad,
    meta: { protected: false, admin: false }
  },
  {
    path: '/admin/olympiad',
    name: 'OlympiadAdmin',
    component: OlympiadAdmin,
    meta: { protected: true, admin: true }
  },
  {
    path: '/contact',
    name: 'Contact',
    component: Contact,
    meta: { protected: false, admin: false }
  },
  {
    path: '/admin/result',
    name: 'ResultAdmin',
    component: ResultAdmin,
    meta: { protected: true, admin: true }
  },
  {
    path: '/admin/reply/:id',
    name: 'ReplyAdmin',
    component: ReplyAdmin,
    meta: { protected: true, admin: true },
    props: true
  },
  {
    path: '/admin/signup/administrator',
    name: 'SignupAdmin',
    component: SignupAdmin,
    meta: { protected: true, admin: true }
  },
  {
    path: '/:pathMatch(.*)*',
    component: NotFound,
    meta: { protected: false, admin: false }
  }
];

const handler_router = createRouter({
  history: createWebHistory(),
  routes,
});
handler_router.beforeEach((to, from, next) => {
  if (to.meta.protected) {
    const URL = to.meta.admin ? '/admin/verification' : '/protected';
    _axios.get(URL).then(response => {
      response.data.session ? next() : next('/login');
    }).catch(error => {
      next('/login');
    });
  } 
  else {
    next();
  }
});

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

const app = createApp(App);
app.use(handler_router);
app.use(pinia);

app.use(ToastPlugin);

app.mount('#app');