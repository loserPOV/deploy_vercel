from fastapi import FastAPI, HTTPException, Request
#cara jalanin di terminal -> uvicorn <nama_file>:<variable_penampung_FastAPI>
import pandas as pd

key = 'secret123'

app = FastAPI()

data = pd.read_csv("data.csv")

@app.get("/data")
def handler():
    return data.to_dict(orient='records')



@app.get("/")
def handler(request: Request):
    headers = request.headers
    #retrieve User-Agent key in headers
    agent = headers.get("User-Agent")
    token = headers.get("Token")

    if token == None:
        raise HTTPException(status_code=500, detail='belum login')
    else:
        if token != key:
            raise HTTPException(status_code=500, detail='key salah')
        else:
            return {
                "message": "Halaman Utama",
                "agent": agent
            }

    


@app.get("/home/{user}")
def handler(user):
    if user == "fajar":
        return {
            "message": "Hello Home",
            "user" : user
        }
    else:
        raise HTTPException(status_code=400, detail="not found")