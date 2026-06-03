from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="FastAPI Project")

class User(BaseModel):
    name: str
    age: int
    role: str

@app.get("/")
def home():
    return {
        "message": "Welcome to my FastAPI project",
        "status": "Running successfully"
    }

@app.get("/about")
def about():
    return {
        "project": "FastAPI Basic Project",
        "purpose": "Learning Python API development"
    }

@app.post("/user")
def create_user(user: User):
    return {
        "message": "User created successfully",
        "user_details": user
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)