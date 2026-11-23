from google import genai
from app.core.config import settings

class GeminiAI:
    client = genai.Client(api_key=settings.GEMINI_API_KEY)
    def __init__(self, input):
        interaction = self.client.interactions.create(model="gemini-3.5-flash-lite", input=input)
        self.output_text = interaction.output_text