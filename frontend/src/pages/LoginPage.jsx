import { useState } from 'react'
import api, { setToken } from '../services/api'

export default function LoginPage({ onAuthenticated }) {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')

  const handleSubmit = async (event) => {
    event.preventDefault()
    setError('')
    try {
      const response = await api.post('/auth/token', { username, password })
      const token = response.data.access_token
      setToken(token)
      onAuthenticated(token)
    } catch (err) {
      setError(err?.response?.data?.detail || 'Login failed')
    }
  }

  return (
    <main className="container">
      <h1>HR Resource Management</h1>
      <form onSubmit={handleSubmit} className="card form-card">
        <h2>Sign In</h2>
        <label>
          Username
          <input value={username} onChange={(e) => setUsername(e.target.value)} />
        </label>
        <label>
          Password
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
        </label>
        {error && <p className="error">{error}</p>}
        <button type="submit">Login</button>
      </form>
    </main>
  )
}
