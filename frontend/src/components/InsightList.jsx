export default function InsightList({ title, items }) {
  return (
    <div className="card">
      <h3>{title}</h3>
      <ul>
        {items?.length ? items.map((item, idx) => <li key={`${title}-${idx}`}>{item}</li>) : <li>No items</li>}
      </ul>
    </div>
  )
}
