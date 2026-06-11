from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.database.db import Base


class MetricSnapshot(Base):
    __tablename__ = "metric_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    metric_type = Column(String(80), nullable=False)
    metric_value = Column(Integer, nullable=False)
    source = Column(String(80), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
