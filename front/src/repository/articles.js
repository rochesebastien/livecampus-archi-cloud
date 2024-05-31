import axios from 'axios'
import { url } from '../config/api'

export async function getArticles () {
    const res = await axios.get(url + 'articles')
    return res.data
}

export async function getArticle(id) {
    const res = await axios.get(url + 'articles/' + id)
    return res.data
}

export async function deleteArticle(id) {
    try {
        await axios.delete(url + 'articles/' + id)
        return true
    } catch {
        return false
    }
}

export async function createArticle(title, content, ranking, blog_id) {
    try {
        const res = await axios.post(url + 'articles', {
            title,
            content,
            ranking,
            blog_id
        })
        return res
    } catch {
        return false
    }
}

export async function updateArticle(id, title, topic, date) {
    try {
        const res = await axios.patch(url + 'articles/' + id, {
            title,
            topic,
            date
        })
        return res
    } catch {
        return false
    }
}