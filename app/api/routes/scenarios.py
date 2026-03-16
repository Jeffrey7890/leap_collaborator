from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.scenario import Scenario
from app.schemas.scenario_schema import ScenarioCreate, ScenarioResponse

router = APIRouter()

@router.post("/", response_model=ScenarioResponse)
def create_scenario(scenario: ScenarioCreate, db: Session = Depends(get_db)):

    new_scenario = Scenario(
        project_id=scenario.project_id,
        name=scenario.name,
        description=scenario.description,
        created_by=1
    )

    db.add(new_scenario)
    db.commit()
    db.refresh(new_scenario)

    return new_scenario


@router.get("/", response_model=list[ScenarioResponse])
def list_scenarios(db: Session = Depends(get_db)):
    return db.query(Scenario).all()