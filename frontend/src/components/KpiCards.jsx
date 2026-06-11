export default function KpiCards({ report }) {
  if (!report) return null

  const productivity = report.productivity || {}
  const climate = report.climate || {}
  const resources = report.resources || {}

  return (
    <div className="grid">
      <div className="card"><h3>Completion Rate</h3><p>{productivity.completion_rate ?? 0}%</p></div>
      <div className="card"><h3>Engagement Avg</h3><p>{climate.engagement_avg ?? 0}</p></div>
      <div className="card"><h3>Stress Avg</h3><p>{climate.stress_avg ?? 0}</p></div>
      <div className="card"><h3>Avg Tasks / Employee</h3><p>{resources.avg_tasks_per_employee ?? 0}</p></div>
    </div>
  )
}
