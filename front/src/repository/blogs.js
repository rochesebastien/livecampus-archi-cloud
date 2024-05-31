import axios from 'axios'
import { url } from '../config/api'

export async function getBlogs () {
    const res = await axios.get(url + 'blogs')
    return res.data
}

export async function getBlog(id) {
    const res = await axios.get(url + 'blogs/' + id)
    return res.data
}

export async function deleteBlog(id) {
    try {
        await axios.delete(url + 'blogs/' + id)
        return true
    } catch {
        return false
    }
}

export async function createBlog(title, topic, date) {
    try {
        const res = await axios.post(url + 'blogs', {
            title,
            topic,
            date
        })
        return res
    } catch {
        return false
    }
}

export async function updateBlog(id, title, topic, date) {
    try {
        const res = await axios.patch(url + 'blogs/' + id, {
            title,
            topic,
            date
        })
        return res
    } catch {
        return false
    }
}