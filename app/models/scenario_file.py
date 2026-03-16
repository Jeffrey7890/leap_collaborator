from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.db.database import Base

class ScenarioFile(Base):
    __tablename__ = "scenario_files"

    id = Column(Integer, primary_key=True, index=True)
    version_id = Column(Integer, ForeignKey("scenario_versions.id"))
    file_path = Column(String, nullable=False)
    uploaded_by = Column(Integer, ForeignKey("users.id"))
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())