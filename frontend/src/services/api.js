import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || 'http://localhost:8000'
})

export function setToken(token) {
  api.defaults.headers.common.Authorization = token
}

export default api
