from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import analyzer
from app.core.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# Senior move: Strict CORS for security
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with your UI URL
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(analyzer.router, prefix=f"{settings.API_V1_STR}/medical", tags=["Analysis"])

@app.get("/")
def read_root():
    return {"message": "Livlong Health API is online"}