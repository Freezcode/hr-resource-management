import { useState } from 'react'
import DashboardPage from './pages/DashboardPage'
import LoginPage from './pages/LoginPage'

export default function App() {
  const [token, setToken] = useState(sessionStorage.getItem('hr_token'))

  const handleAuthenticated = (authToken) => {
    sessionStorage.setItem('hr_token', authToken)
    setToken(authToken)
  }

  if (!token) {
    return <LoginPage onAuthenticated={handleAuthenticated} />
  }

  return <DashboardPage />
}
