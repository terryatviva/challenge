import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Axios from './plugins/axios';
import iView from 'iview';
import locale from 'iview/dist/locale/en-US';
import 'iview/dist/styles/iview.css';
import '../node_modules/bootstrap/dist/css/bootstrap.css';
import '../node_modules/font-awesome/css/font-awesome.min.css';

Vue.config.productionTip = false
Vue.use(Axios);
Vue.use(iView, { locale });

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
