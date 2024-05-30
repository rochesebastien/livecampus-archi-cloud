<template>
    <v-divider></v-divider>
    <h3 class="mt-2">Bienvenue sur le blog {{ blog.title }}</h3>
    <h4 v-if="blog.articles.length !== 0">Consultez {{ blog.articles.length <= 1 ? "son unique article" : `ses ${blog.articles.length} articles` }} ci-dessous :</h4>
    <h4 v-else>Le blog n'a pas encore d'article !</h4>
</template>
<script setup>
import { useRoute } from 'vue-router'

const route = useRoute()
const id = route.params.id

const blog = {
    title: 'InformatiK',
    articles: ['a', 'b']
}
</script>