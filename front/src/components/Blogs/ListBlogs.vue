<template>
    <v-card flat>
        <template v-slot:text>
            <v-text-field v-model="search" label="Rechercher un blog..." prepend-inner-icon="mdi-magnify" variant="outlined"
                hide-details single-line></v-text-field>
        </template>

        <v-data-table :headers="headers" :items="articles" :search="search">
            <template v-slot:item.actions="{ item }">
                <ActionsMenu :items="actions" />
            </template>
        </v-data-table>
    </v-card>
</template>
<script setup>
import { ref } from 'vue'

const search = ref('')
const headers = [
    {
        align: 'start',
        key: 'title',
        title: 'Titre',
    },
    { key: 'topic', title: 'Sujet' },
    { key: 'date', title: 'Date de création' },
    { key: 'articles_quantity', title: 'Nombre d\'article(s)' },
    { key: 'actions', title: 'Actions', align: 'end' }
]
const articles = [
    {
        title: 'Informatik',
        topic: "Tous les sujets sur l'informatique.",
        date: '30/05/2024',
        articles_quantity: '6'
    }
]
const actions = [
    {
        title: 'Modifier',
        action: 'update'
    },
    {
        title: 'Supprimer',
        action: 'delete'
    }
]
</script>