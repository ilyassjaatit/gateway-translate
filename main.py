from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

class Translation(BaseModel):
    text:str
    translated_text: str
    source_language: str
    target_language: str


app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}