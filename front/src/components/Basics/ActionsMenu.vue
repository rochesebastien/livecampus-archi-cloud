<template>
    <v-menu>
        <template v-slot:activator="{ props }">
            <v-btn density="compact" elevation="0" icon="mdi-dots-vertical" v-bind="props" />
        </template>
        <v-list>
            <v-list-item v-for="(item, index) in items" :key="index" :value="index">
                <v-list-item-title @click="emit('click:item', item.action)">{{ item.title }}</v-list-item-title>
            </v-list-item>
        </v-list>
    </v-menu>
</template>
<script setup>
defineProps({
    items: {
        type: Array,
        required: true
    }
})

const emit = defineEmits(['click:item'])
</script>