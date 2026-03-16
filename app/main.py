from fastapi import FastAPI
from app.api.api_router import router
from app.db.database import Base, engine

# Import models so SQLAlchemy knows them
from app.models import user, project, scenario, scenario_version, scenario_result

app = FastAPI(title="Collaborative LEAP Scenario Tracking Platform")

Base.metadata.create_all(bind=engine)

app.include_router(router)