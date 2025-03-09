from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Ultimate AI Assistant!"}

@app.get("/ask/{query}")
def ask_ai(query: str):
    """Runs LLaMA AI model and returns response"""
    result = subprocess.run(["ollama", "run", "llama3", query], capture_output=True, text=True)
    return {"response": result.stdout}
