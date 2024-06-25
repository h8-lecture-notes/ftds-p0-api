# Import package
from fastapi import FastAPI, HTTPException
import pandas as pd

# olah file csv -> DataFrame
df = pd.read_csv("users.csv")

# create FastAPI object
app = FastAPI()

# contoh url:
# google.com/ -> url /
# localhost == 127.0.0.1

# create endpoint/url
# define method and url
@app.get("/")
def handler(): # handler
    # return a response (data + status code)
    return df.to_dict(orient="records") # status code -> 200

# define method and url w/dynamic parameter
@app.get("/profile/{name}")
def handler(name: str):
    # filtering data
    filter = df[df['name'] == name]

    # error/exception handling
    if len(filter) == 0:
        raise HTTPException(status_code=404, detail="data not found")
    
    # return data
    return filter.to_dict(orient="records") # "john cena" -> data "john cena"