from fastapi import FastAPI

app = FastAPI(title="Agentic AI Platform")

@app.get("/")
async def root():
    return {
        "status": "Running",
        "version": "1.0.0"
    }