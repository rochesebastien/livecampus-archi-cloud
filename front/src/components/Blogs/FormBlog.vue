<template>
    <v-form v-model="form">
        <v-text-field :rules="[require]" v-model="name" :placeholder="'Nom du blog'" />
        <v-text-field :rules="[require]" v-model="topic" :placeholder="'Sujet'" />
        <v-btn @click="onClickButton" :disabled="!form" class="w-100" color="white">{{ id ? 'Modifier le blog' : 'Créer le blog' }}</v-btn>
    </v-form>
</template>
<script setup>
import { ref } from 'vue'
import { require } from '../helper/rules';
import { useRoute } from 'vue-router'

const route = useRoute()
const id = route.params?.id

const form = ref()
const name = ref()
const topic = ref()

// Methods
function onClickButton () {
    if (id) {
        alert('update ' + id)
    } else {
        alert('create')
    }
}
</script>