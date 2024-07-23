import Vue from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import bootstrap from 'bootstrap/dist/js/bootstrap.bundle.js';

Vue.config.productionTip = false;

new Vue({
    router,
    render: h => h(App),
    bootstrap
}).$mount('#app');
