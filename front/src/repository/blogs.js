import axios from 'axios'
import { url } from '../config/api'

export async function getBlogs () {
    const res = await axios.get(url + 'blogs')
    return res.data
}

export function getBlog(id) {
    axios.get(url + 'blogs/' + id).then((res, req) => {
        return res.data
    })
}

export async function deleteBlog(id) {
    try {
        await axios.delete(url + 'blogs/' + id)
        return true
    } catch {
        return false
    }
}