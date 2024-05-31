<template>
    <v-form v-model="form">
        <v-text-field :rules="[require]" v-model="name" :placeholder="'Nom du blog'" />
        <v-text-field :rules="[require]" v-model="topic" :placeholder="'Sujet'" />
        <v-btn @click="onClickButton" :disabled="!form" class="w-100" color="white">{{ id ? 'Modifier le blog' : 'Créer le blog' }}</v-btn>
    </v-form>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { require } from '../helper/rules';
import { useRoute, useRouter } from 'vue-router'
import { createBlog, getBlog, updateBlog } from '@/repository/blogs';

const route = useRoute()
const router = useRouter()
const id = route.params?.id

const form = ref()
const name = ref()
const topic = ref()

// Methods
async function onClickButton () {
    if (id) {
        await updateBlog(id, name.value, topic.value, '2024-05-31')
        router.push({
            path: '/blogs'
        })
    } else {
        await createBlog(name.value, topic.value, '2024-05-31')
        router.push({
            path: '/blogs'
        })
    }
}

onMounted(async () => {
    const blog = await getBlog(id)
    name.value = blog.title
    topic.value = blog.topic
})
</script>