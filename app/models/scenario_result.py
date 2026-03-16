from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app.db.database import Base

class ScenarioResult(Base):
    __tablename__ = "scenario_results"

    id = Column(Integer, primary_key=True, index=True)
    version_id = Column(Integer, ForeignKey("scenario_versions.id"))
    year = Column(Integer, nullable=False)
    variable = Column(String, nullable=False)
    sector = Column(String)
    value = Column(Float, nullable=False)
    unit = Column(String)