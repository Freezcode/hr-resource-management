import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from 'recharts'

export default function ClimateChart({ climate }) {
  const data = [
    { name: 'Engagement', value: climate?.engagement_avg ?? 0 },
    { name: 'Stress', value: climate?.stress_avg ?? 0 }
  ]

  return (
    <div className="card chart-card">
      <h3>Climate Metrics</h3>
      <ResponsiveContainer width="100%" height={260}>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis domain={[0, 10]} />
          <Tooltip />
          <Bar dataKey="value" fill="#4f46e5" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  )
}
