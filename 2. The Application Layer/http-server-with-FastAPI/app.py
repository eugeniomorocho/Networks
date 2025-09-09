# app.py
from fastapi import FastAPI, Response, Request

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, GET request!"}

@app.post("/submit")
def submit_data(data: dict):
    return {"received": data}

@app.get("/cookie")
def set_cookie(response: Response):
    response.set_cookie(key="user", value="student123")
    return {"message": "Cookie set!"}