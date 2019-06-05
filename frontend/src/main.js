import Vue from 'vue'
import App from './App'
import router from './router'
import store from './store'
import * as backendAPI from './common/backendAPI'
import VueResource from 'vue-resource'
import VModal from 'vue-js-modal'

import 'bootstrap'

Vue.use(VModal)
Vue.use(VueResource)

Vue.config.productionTip = false

Vue.prototype.$api = backendAPI

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
