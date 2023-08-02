from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

origins = [
    "*"
]
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

result = list()

@app.get("/")
async def run(city, salary, degree, company):
    rs = ["Java开发工程师", city, company, degree, salary]
    global result
    result.append(rs)
    return "OK"

@app.get("/list")
async def print():
    global result
    return result

@app.get("/save")
async def save(name: str):
    global result
    df = pd.DataFrame(result)
    df.to_csv(f"./{name}.csv")
    result = list()
    return "OK"
