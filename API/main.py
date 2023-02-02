import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel


# with open("../Files/xgbModel.pkl", 'rb') as file:
with open("xgbModel.pkl", 'rb') as file:
    xgb = pickle.load(file)


app = FastAPI()

class TextIn(BaseModel):
    State: str
    BankState: str
    NAICS: str
    ApprovalFY : int
    Term : int
    NoEmp : int
    GrAppv : float
    NewExist : str
    CreateJob : int
    RetainedJob : int
    Franchise : str
    UrbanRural : str

class Prediction(BaseModel):
    MIS_Status : int
    

@app.post("/predict", response_model = Prediction)
async def predict(payload:TextIn):
    new_payload=pd.DataFrame(dict(payload),index = [0])
    class_idx=xgb.predict(new_payload)[0]
    return {'MIS_Status':int(class_idx)}

# uvicorn main:app --reload
