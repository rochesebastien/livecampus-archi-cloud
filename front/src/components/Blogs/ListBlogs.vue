<template>
    <v-card flat>
        <template v-slot:text>
            <v-text-field v-model="search" label="Rechercher un blog..." prepend-inner-icon="mdi-magnify"
                variant="outlined" hide-details single-line></v-text-field>
        </template>

        <v-data-table :headers="headers" :items="articles" :search="search">
            <template v-slot:item.actions="{ item }">
                <ActionsMenu @click:item="onClickItem($event, item.id)" :items="actions" />
            </template>
        </v-data-table>
    </v-card>
    <v-dialog v-model="deleteDialog" width="auto">
        <v-card max-width="400" prepend-icon="mdi-delete" text="Êtes-vous sûr de vouloir supprimer ce blog ?"
            title="Suppression de blog">
            <div class="d-flex justify-end pa-1">
                <v-btn color="info" text="Annuler" @click="deleteDialog = false"></v-btn>
                <v-btn class="ms-1" color="error" text="Supprimer" @click="deleteDialog = false; onDeleteBlog()"></v-btn>
            </div>
        </v-card>
    </v-dialog>
</template>
<script setup>
import { ref } from 'vue'

const deleteDialog = ref()
const selectedItem = ref()

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
        title: 'Modifier',
        action: 'update'
    },
    {
        title: 'Supprimer',
        action: 'delete'
    },
    {
        title: 'Afficher',
        action: 'show'
    }
]

// Methods
function onClickItem (action, item) {
    selectedItem.value = item
    switch (action) {
        case 'delete':
            deleteDialog.value = true
            break;
        case 'update':
            break;
        case 'show':
            break;
    }
    console.log(action, item);
}

function onDeleteBlog() {
    alert('Suppression de ' + selectedItem.value)
}
</script>