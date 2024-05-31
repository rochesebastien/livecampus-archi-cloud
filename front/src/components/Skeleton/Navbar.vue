<template>
    <v-card>
        <v-layout>
            <v-navigation-drawer expand-on-hover rail>
                <v-list>
                    <v-list-item title="FastAPI" subtitle="Interface web pour FastAPI"></v-list-item>
                </v-list>

                <v-divider></v-divider>

                <!-- Default routes -->
                <v-list density="compact" nav>
                    <RouterLink v-for="route in navbarDefaultRoutes" :to="route.href" style="text-decoration: none; color: inherit;"><v-list-item :prepend-icon="route.icon" :title="route.title"></v-list-item></RouterLink>
                </v-list>

                <v-divider v-if="navbarBlogRoutes.length > 0"></v-divider>

                <!-- Blogs routes -->
                <v-list density="compact" nav>
                    <RouterLink v-for="route in navbarBlogRoutes" :to="route.href" style="text-decoration: none; color: inherit;"><v-list-item :prepend-icon="route.icon" :title="route.title"></v-list-item></RouterLink>
                </v-list>

                <v-divider v-if="navbarArticleRoutes.length > 0"></v-divider>

                <!-- Articles routes -->
                <v-list density="compact" nav>
                    <RouterLink v-for="route in navbarArticleRoutes" :to="route.href" style="text-decoration: none; color: inherit;"><v-list-item :prepend-icon="route.icon" :title="route.title"></v-list-item></RouterLink>
                </v-list>

                <!-- <v-list density="compact" nav>
                    <v-list-item prepend-icon="mdi-folder" title="Les blogs" value="myfiles"></v-list-item>
                    <v-list-item prepend-icon="mdi-account-multiple" title="Shared with me"
                        value="shared"></v-list-item>
                    <v-list-item prepend-icon="mdi-star" title="Starred" value="starred"></v-list-item>
                </v-list> -->
            </v-navigation-drawer>

            <v-main style="height: 100vh;">
                <slot name="main" />
            </v-main>
        </v-layout>
    </v-card>
</template>
<script setup>
import { navbarDefaultRoutes, navbarArticleRoutes, navbarBlogRoutes } from '@/router/routes';
</script>