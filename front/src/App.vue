<template>
  <v-app>
    <Navbar>
      <template #main>
        <v-breadcrumbs :items="route.meta.breadcrumb"></v-breadcrumbs>
        <div class="px-4">
          <h1>{{ route.meta.title }}</h1>
          <RouterView />
        </div>
      </template>
    </Navbar>

    <AppFooter />
  </v-app>
</template>
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
</script>