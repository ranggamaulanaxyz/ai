from fastapi import FastAPI
from workers import WorkerEntrypoint, asgi
from app.core.config import settings
from app.services.gemini import GeminiAI

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)


@app.get("/")
async def root():
    ai = GeminiAI(input="Hai")
    return {"output": ai.output_text}


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return await asgi.fetch(app, request, self.env)
