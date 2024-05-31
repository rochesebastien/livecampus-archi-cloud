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

export function deleteBlog(id) {
    axios.delete(url + 'blogs/' + id).then((res, req) => {
        console.log(res);
    })
}