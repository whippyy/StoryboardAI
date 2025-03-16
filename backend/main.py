from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message" : "AI storyboard backend is running"}
