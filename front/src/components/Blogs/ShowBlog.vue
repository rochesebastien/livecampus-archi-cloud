<template>
    <v-divider></v-divider>
    <h3 class="mt-2">Bienvenue sur le blog {{ blog.title }}</h3>
    <h4 v-if="blog.articles.length !== 0">Consultez {{ blog.articles.length <= 1 ? "son unique article" : `ses ${blog.articles.length} articles` }} ci-dessous :</h4>
    <h4 v-else>Le blog n'a pas encore d'article !</h4>
    <v-card flat>
        <template v-slot:text>
            <v-text-field v-model="search" label="Rechercher un article..." prepend-inner-icon="mdi-magnify"
                variant="outlined" hide-details single-line></v-text-field>
        </template>

        <v-data-table :headers="headers" :items="articles" :search="search">
            <template v-slot:item.actions="{ item }">
                <ActionsMenu @click:item="onClickItem($event, item.id)" :items="actions" />
            </template>
        </v-data-table>
    </v-card>
    <v-dialog v-model="deleteDialog" width="auto">
        <v-card max-width="400" prepend-icon="mdi-delete" text="Êtes-vous sûr de vouloir supprimer cet article ?"
            title="Suppression de blog">
            <div class="d-flex justify-end pa-1">
                <v-btn color="info" text="Annuler" @click="deleteDialog = false"></v-btn>
                <v-btn class="ms-1" color="error" text="Supprimer" @click="deleteDialog = false; onDeleteArticle()"></v-btn>
            </div>
        </v-card>
    </v-dialog>
</template>
<script setup>
import { ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'

const router = useRouter()

const route = useRoute()
const id = route.params.id

const blog = {
    title: 'InformatiK',
    articles: ['a', 'b']
}

const deleteDialog = ref()
const selectedItem = ref()

const search = ref('')
const headers = [
    {
        align: 'start',
        key: 'title',
        title: 'Titre',
    },
    { key: 'content', title: 'Contenu' },
    { key: 'ranking', title: 'Notation' },
    { key: 'actions', title: 'Actions', align: 'end' }
]
const articles = [
    {
        id: 1,
        title: 'Informatik',
        topic: "Tous les sujets sur l'informatique.",
        date: '30/05/2024',
        articles_quantity: 7
    },
    {
        id: 2,
        title: 'Informatik',
        topic: "Tous les sujets sur l'informatique.",
        date: '30/05/2024',
        articles_quantity: 7
    }
]
const actions = [
    {
        title: 'Supprimer',
        action: 'delete'
    }
]

// Methods
function onClickItem (action, item) {
    selectedItem.value = item
    switch (action) {
        case 'delete':
            deleteDialog.value = true
            break;
    }
}

function onDeleteArticle() {
    alert('Suppression de ' + selectedItem.value)
}
</script>