from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.db.database import engine, Base
from app.api.routes.chapters import router as chapters_router
from app.api.routes.exams import router as exams_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chapters_router)
app.include_router(exams_router)


@app.get("/api/health")
def health_check():
    return {"status": "ok", "message": "Ο server λειτουργεί κανονικά"}
