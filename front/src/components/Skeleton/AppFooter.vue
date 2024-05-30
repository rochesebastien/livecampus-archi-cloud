<template>
  <v-footer height="40" class="footer" app>
    <a
      v-for="item in items"
      :key="item.title"
      :href="item.href"
      :title="item.title"
      class="d-inline-block mx-2 social-link"
      rel="noopener noreferrer"
      target="_blank"
    >
      <v-icon
        :icon="item.icon"
        :size="item.icon === '$vuetify' ? 24 : 16"
      />
    </a>

    <div
      class="text-caption text-disabled"
      style="position: absolute; right: 16px;"
    >
      &copy; 2024 <span class="d-none d-sm-inline-block">Quentin Rodrigues Sébastien Roche</span>
    </div>
  </v-footer>
</template>

<script setup>
  const items = [
    {
      title: 'Code source',
      icon: `mdi-github`,
      href: 'https://github.com/rochesebastien/livecampus-archi-cloud',
    }
  ]
</script>

<style scoped>
  .social-link {
    color: rgba(var(--v-theme-on-background), var(--v-disabled-opacity));
    text-decoration: none;
    transition: .2s ease-in-out
  }

  .social-link:hover {
    color: rgba(25, 118, 210, 1);
  }

  .footer {
    background: rgb(18,18,18)
  }
</style>
