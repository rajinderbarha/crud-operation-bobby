from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app= FastAPI()

class tea(BaseModel):
    id : int 
    name : str
    origin: str

teas :list[tea]=[]

@app.get("/")
def read_root():
    return{"message":"welcome to tea house"}
@app.get("/teas")
def get_teas():
    return teas
@app.post("/teas")
def add_tea(tea:tea):
    teas.append(tea)
    return{"message":"sucessfull"}
@app.put("/teas/{tea_id}")
def update_tea(tea_id: int,updated_tea:tea):
    for index,tea in enumerate(teas):
        if tea_id == tea_id:
            teas[index]= update_tea
            return update_tea
    return {"meassge":"tea is not found"}
@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index,tea in enumerate(teas):
        if tea_id == tea_id:
           deleted = teas.pop(index)
           return deleted
    return {"error":"tea not found"}    
            


    

    
