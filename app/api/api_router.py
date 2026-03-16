from fastapi import APIRouter
from app.api.routes import users, projects, scenarios, uploads

router = APIRouter()
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(projects.router, prefix="/projects", tags=["Projects"])
router.include_router(scenarios.router, prefix="/scenarios", tags=["Scenarios"])
router.include_router(uploads.router, prefix="/uploads", tags=["Uploads"])