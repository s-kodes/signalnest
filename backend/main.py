from fastapi import FastAPI

app = FastAPI(title="SignalNest API")


@app.get("/")
def home():
    return {"message": "Welcome to SignalNest!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
