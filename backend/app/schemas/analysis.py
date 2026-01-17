from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    filename: str
    analysis: str
    status: str = "success"