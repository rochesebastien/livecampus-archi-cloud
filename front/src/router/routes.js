// Default
import Home from '../components/Home.vue'

// Blogs
import ListBlogs from '../components/Blogs/ListBlogs'
import FormBlog from '@/components/Blogs/FormBlog.vue'
import ShowBlog from '@/components/Blogs/ShowBlog.vue'

// Articles

const routes = [
    // Default
    {
        path: '/',
        component: Home,
        meta: { title: 'Accueil', breadcrumb: ['Accueil'] }
    },
    // Blogs
    {
        path: '/blogs',
        component: ListBlogs,
        meta: { title: 'Liste des blogs', breadcrumb: ['Accueil', 'Blogs'] }
    },
    {
        path: '/blog/:id',
        component: ShowBlog,
        meta: { title: 'Afficher un blog', breadcrumb: ['Accueil', 'Blog'] }
    },
    {
        path: '/blog/new',
        component: FormBlog,
        meta: { title: 'Créer un blog', breadcrumb: ['Accueil', 'Blog', 'Nouveau'] }
    },
    {
        path: '/blog/update/:id',
        component: FormBlog,
        meta: { title: 'Modifier un blog', breadcrumb: ['Accueil', 'Blog', 'Modifier'] }
    }
]

// Routes for navbar
export const navbarDefaultRoutes = [
    {
        icon: 'mdi-home',
        title: 'Accueil',
        href: '/'
    }
]

export const navbarBlogRoutes = [
    {
        icon: 'mdi-post',
        title: 'Les blogs',
        href: '/blogs'
    },
    {
        icon: 'mdi-plus',
        title: 'Créer un blog',
        href: '/blog/new'
    }
]

export const navbarArticleRoutes = []

export default routes