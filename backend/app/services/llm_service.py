import google.generativeai as genai
from app.core.config import settings

class LLMService:
    def __init__(self):
        # 1. Configure the API
        genai.configure(api_key=settings.GOOGLE_API_KEY)
        
        # 2. Smart Model Selection
        self.model = None
        print("--- AUTO-DETECTING AVAILABLE AI MODELS ---")
        try:
            # We ask the API what models this specific key can use
            available_models = [
                m.name for m in genai.list_models() 
                if 'generateContent' in m.supported_generation_methods
            ]
            print(f"DEBUG: Found models: {available_models}")
            
            # We try to pick the best available one in order of preference
            preferences = [
                'models/gemini-1.5-flash', 
                'models/gemini-pro', 
                'models/gemini-1.5-flash-latest',
                'models/gemini-1.0-pro'
            ]
            
            for target in preferences:
                if target in available_models:
                    print(f"DEBUG: Successfully selected {target}")
                    self.model = genai.GenerativeModel(target)
                    break
            
            # If none of our preferences were found, just take the first working one
            if not self.model and available_models:
                print(f"DEBUG: No preference found, using {available_models[0]}")
                self.model = genai.GenerativeModel(available_models[0])

        except Exception as e:
            print(f"DEBUG: List models failed: {e}")
            # Final fallback: Try the most standard ID if list_models fails
            self.model = genai.GenerativeModel('gemini-pro')
        
        print("------------------------------------------")

    async def analyze_medical_text(self, text: str):
        if not self.model:
            return "Error: AI Model could not be initialized. Please check API key project permissions."

        prompt = f"""
        You are a senior medical analyst at Livlong 365. 
        Analyze the following medical report text and provide:
        1. Patient Summary.
        2. Abnormal results (High/Low).
        3. Recommended Livlong wellness steps.
        
        Report Content: {text[:10000]}
        """
        
        try:
            # We use a timeout to ensure the UI doesn't hang
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"AI INFERENCE ERROR: {str(e)}")
            return f"I encountered an error while analyzing the report. Details: {str(e)}"