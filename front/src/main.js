/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Router
import { createWebHistory, createRouter } from 'vue-router'
import routes from './router/routes'

const router = createRouter({
    history: createWebHistory(),
    routes
})

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'

const app = createApp(App)

registerPlugins(app)

app.use(router).mount('#app')
