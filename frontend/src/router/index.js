import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Admin from '../components/Admin.vue'
import AfterSubmission from '../components/AfterSubmission.vue'
import UserForm from '../components/UserForm.vue'

Vue.use(VueRouter)

export const router = new VueRouter({
    mode: 'history',
    routes: [
      {path: '/', component: Home},
      {path: '/user-form', component: UserForm},
      {path: '/admin', component: Admin},
      {path: '/complete', component: AfterSubmission},
    ]
})
  