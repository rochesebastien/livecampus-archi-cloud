// Default
import Home from '../components/Home.vue'

// Blogs
import ListBlogs from '../components/Blogs/ListBlogs'
import AddBlog from '@/components/Blogs/AddBlog.vue'

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
        path: '/blog/new',
        component: AddBlog,
        meta: { title: 'Ajouter un blog', breadcrumb: ['Accueil', 'Nouveau'] }
    },
    // Articles
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

export const navbarArticleRoutes = [
    {
        icon: 'mdi-file',
        title: 'Les articles',
        href: '/articles'
    },
    {
        icon: 'mdi-plus',
        title: 'Créer un article',
        href: '/article/new'
    }
]

export default routes