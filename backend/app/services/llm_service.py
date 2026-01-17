from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from app.core.config import settings

class LLMService:
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_key=settings.OPENAI_API_KEY,
            model="gpt-3.5-turbo",
            temperature=0
        )

    async def analyze_medical_text(self, text: str):
        system_msg = SystemMessage(content="""
            You are a senior medical analyst at Livlong 365. 
            Extract structured data from report text. Include:
            1. Patient Summary.
            2. Abnormal results (High/Low).
            3. Recommended Livlong wellness steps (e.g., 'Consult a Cardiologist', 'Book a follow-up lab test').
            Keep it professional and concise.
        """)
        
        human_msg = HumanMessage(content=f"Report Content: {text[:8000]}")
        
        response = await self.llm.ainvoke([system_msg, human_msg])
        return response.content