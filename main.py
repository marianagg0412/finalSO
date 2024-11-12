from fastapi import FastAPI, Request
from pydantic import BaseModel
import json
import os

app = FastAPI()

class UserInfo(BaseModel):
    name: str
    age: int
    profession: str

    class Config: #Para brindar un ejemplo
        schema_extra = {
            "example": {
                "name": "John Doe",
                "age": 30,
                "profession": "Engineer"
            }
        }



@app.post("/store_info")
async def store_info(user_info: UserInfo):
    file_name = f"{user_info.name}_{user_info.age}.json"
    file_path = f"./stored_files/{file_name}"
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w") as f:
        json.dump(user_info.model_dump(), f)

    return {"message": f"Data stored successfully in {file_path}"}
