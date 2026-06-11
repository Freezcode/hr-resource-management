import ClimateChart from '../components/ClimateChart'
import InsightList from '../components/InsightList'
import KpiCards from '../components/KpiCards'
import useDashboard from '../hooks/useDashboard'

export default function DashboardPage() {
  const { data, loading, error } = useDashboard()

  if (loading) return <main className="container"><p>Loading dashboard...</p></main>
  if (error) return <main className="container"><p className="error">{error}</p></main>

  const report = data?.report || {}
  const plan = data?.action_plan || {}

  return (
    <main className="container">
      <h1>Executive Dashboard</h1>
      <KpiCards report={report} />
      <ClimateChart climate={report.climate} />
      <div className="grid">
        <InsightList title="Productivity Insights" items={report.productivity?.insights} />
        <InsightList title="Climate Recommendations" items={report.climate?.recommendations} />
        <InsightList title="Resource Actions" items={report.resources?.actions} />
        <InsightList title="Action Plan" items={plan.priority_actions} />
      </div>
    </main>
  )
}
