<template>
    <v-card flat v-if="!loading">
        <template v-slot:text>
            <v-text-field v-model="search" label="Rechercher un blog..." prepend-inner-icon="mdi-magnify"
                variant="outlined" hide-details single-line></v-text-field>
        </template>

        <v-data-table :headers="headers" :items="_blogs" :search="search">
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
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { getBlogs } from '../../repository/blogs'

const router = useRouter()

const deleteDialog = ref()
const selectedItem = ref()
const loading = ref(true)

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
const blogs = ref([])

const actions = [
    {
        title: 'Afficher',
        action: 'show'
    },
    {
        title: 'Modifier',
        action: 'update'
    },
    {
        title: 'Supprimer',
        action: 'delete'
    }
]

// Computed
const _blogs = computed(() => {
    return blogs.value.map(blog => ({...blog, articles_quantity: blog.articles.length, date: formatDate(blog.date)}))
})

// Methods
function onClickItem (action, item) {
    selectedItem.value = item
    switch (action) {
        case 'delete':
            deleteDialog.value = true
            break;
        case 'update':
            router.push({
                path: `/blog/update/${item}`
            })
            break;
        case 'show':
            router.push({
                path: `/blog/${item}`
            })
            break;
    }
}

function onDeleteBlog() {
    alert('Suppression de ' + selectedItem.value)
}

function formatDate(dateParam) {
    let date = new Date(dateParam)
    let day = date.getDate();
    let month = date.getMonth() + 1
    let year = date.getFullYear();

    if (day < 10) {
        day = '0' + day;
    }
    if (month < 10) {
        month = '0' + month;
    }

    return day + '/' + month + '/' + year;
}

// onMounted
onMounted(async () => {
    blogs.value = await getBlogs()
    loading.value = false
})
</script>