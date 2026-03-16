from pydantic import BaseModel

class ScenarioCreate(BaseModel):
    project_id: int
    name: str
    description: str

class ScenarioResponse(BaseModel):
    id: int
    project_id: int
    name: str
    description: str
    created_by: int

    class Config:
        from_attributes = True