from fastapi import FastAPI
from workers import WorkerEntrypoint, asgi
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)


@app.get("/")
async def root():
    return {"message": "Hello from FastAPI on Cloudflare Workers!"}


class Default(WorkerEntrypoint):
    async def fetch(self, request):
        return await asgi.fetch(app, request, self.env)
