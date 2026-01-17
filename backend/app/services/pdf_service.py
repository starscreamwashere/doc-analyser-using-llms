import io
from pypdf import PdfReader
from fastapi import HTTPException

class PDFService:
    @staticmethod
    async def extract_text(file) -> str:
        try:
            content = await file.read()
            pdf_reader = PdfReader(io.BytesIO(content))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() or ""
            
            if not text.strip():
                raise HTTPException(status_code=400, detail="PDF is empty or contains only images.")
            
            return text
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"PDF Parsing Error: {str(e)}")