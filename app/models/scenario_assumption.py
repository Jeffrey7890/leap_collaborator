from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class ScenarioAssumption(Base):
    __tablename__ = "scenario_assumptions"

    id = Column(Integer, primary_key=True, index=True)
    version_id = Column(Integer, ForeignKey("scenario_versions.id"))
    parameter_name = Column(String, nullable=False)
    value = Column(String, nullable=False)
    unit = Column(String)