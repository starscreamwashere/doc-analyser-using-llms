from fastapi import APIRouter, UploadFile, File, Depends
from app.services.pdf_service import PDFService
from app.services.llm_service import LLMService
from app.schemas.analysis import AnalysisResponse

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
async def analyze_doc(
    file: UploadFile = File(...),
    pdf_service: PDFService = Depends(),
    llm_service: LLMService = Depends()
):
    text = await pdf_service.extract_text(file)
    analysis_result = await llm_service.analyze_medical_text(text)
    
    return AnalysisResponse(
        filename=file.filename,
        analysis=analysis_result
    )