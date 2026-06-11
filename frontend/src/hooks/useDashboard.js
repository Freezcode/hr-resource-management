import { useEffect, useState } from 'react'
import api from '../services/api'

export default function useDashboard() {
  const [data, setData] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  useEffect(() => {
    const run = async () => {
      setLoading(true)
      setError('')
      try {
        const response = await api.get('/reports/dashboard')
        setData(response.data)
      } catch (err) {
        setError(err?.response?.data?.detail || 'Unable to load dashboard data')
      } finally {
        setLoading(false)
      }
    }

    run()
  }, [])

  return { data, loading, error }
}
