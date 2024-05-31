<template>
    <div v-if="!loading">
        <v-divider></v-divider>
        <h3 class="mt-2">Bienvenue sur le blog {{ blog.title }}</h3>
        <h4 v-if="blog.articles.length !== 0">Consultez {{ blog.articles.length <= 1 ? "son unique article" : `ses
                ${blog.articles.length} articles` }} ci-dessous :</h4>
                <h4 v-else>Le blog n'a pas encore d'article !</h4>
                <v-card flat>
                    <template v-slot:text>
                        <v-text-field v-model="search" label="Rechercher un article..." prepend-inner-icon="mdi-magnify"
                            variant="outlined" hide-details single-line></v-text-field>
                    </template>

                    <div class="d-flex justify-end">
                        <v-btn color="primary" @click="addDialog = true">Ajouter un article</v-btn>
                    </div>
                    <v-data-table :headers="headers" :items="blog.articles" :search="search">
                        <template v-slot:item.actions="{ item }">
                            <ActionsMenu @click:item="onClickItem($event, item.id)" :items="actions" />
                        </template>
                    </v-data-table>
                </v-card>
                <v-dialog v-model="deleteDialog" width="auto">
                    <v-card max-width="400" prepend-icon="mdi-delete"
                        text="Êtes-vous sûr de vouloir supprimer cet article ?" title="Suppression de blog">
                        <div class="d-flex justify-end pa-1">
                            <v-btn color="info" text="Annuler" @click="deleteDialog = false"></v-btn>
                            <v-btn class="ms-1" color="error" text="Supprimer"
                                @click="deleteDialog = false; onDeleteArticle()"></v-btn>
                        </div>
                    </v-card>
                </v-dialog>
                <v-dialog v-model="addDialog" width="auto">
                    <v-card max-width="400" prepend-icon="mdi-plus" title="Création d'un article">
                        <v-form class="pa-4" v-model="addForm">
                            <v-text-field v-model="addTitle" :rules="[require]" :placeholder="'Nom de l\'article'" />
                            <v-text-field v-model="addContent" :rules="[require]" :placeholder="'Contenu'" />
                        </v-form>
                        <div class="d-flex justify-end pa-1">
                            <v-btn color="error" text="Annuler" @click="addDialog = false"></v-btn>
                            <v-btn :disabled="!addForm" class="ms-1" color="success" text="Créer"
                                @click="addDialog = false; addArticle()"></v-btn>
                        </div>
                    </v-card>
                </v-dialog>
    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import { getBlog } from '@/repository/blogs';
import { deleteArticle, createArticle } from '@/repository/articles'
import { require } from '../helper/rules';

const route = useRoute()
const id = route.params.id

const blog = ref()
const loading = ref(true)
const addForm = ref()

const addTitle = ref()
const addContent = ref()

const deleteDialog = ref()
const addDialog = ref()
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

const actions = [
    {
        title: 'Supprimer',
        action: 'delete'
    }
]

// Methods
function onClickItem(action, item) {
    selectedItem.value = item
    switch (action) {
        case 'delete':
            deleteDialog.value = true
            break;
    }
}

async function onDeleteArticle() {
    const deleted = await deleteArticle(selectedItem.value)
    if (deleted) blog.value.articles = blog.value.articles.filter(article => article.id != selectedItem.value)
}

async function addArticle() {
    await createArticle(addTitle.value, addContent.value, 5, id)
    blog.value = await getBlog(id)
}

// Lifecycle
onMounted(async () => {
    blog.value = await getBlog(id)
    loading.value = false
})
</script>