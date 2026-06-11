import { useState } from 'react'
import DashboardPage from './pages/DashboardPage'
import LoginPage from './pages/LoginPage'

export default function App() {
  const [token, setToken] = useState(localStorage.getItem('hr_token'))

  const handleAuthenticated = (authToken) => {
    localStorage.setItem('hr_token', authToken)
    setToken(authToken)
  }

  if (!token) {
    return <LoginPage onAuthenticated={handleAuthenticated} />
  }

  return <DashboardPage />
}
