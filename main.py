from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "status": "drowsiness api running",
        "note": "model not loaded yet"
    }
