from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Agent Orchestrator 2026")

@app.get("/")
def health():
    return {"status": "running", "version": "v2"}

@app.post("/run")
def run_task(prompt: str):
    return {"status": "ok", "agent": "default", "result": f"รับงานแล้ว: {prompt}"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
