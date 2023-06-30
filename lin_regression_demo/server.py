#!/usr/bin/env python3

import frontend
from fastapi import FastAPI, Request
import os
import uvicorn


app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': 'World4'}




@app.post("/myapi")
async def my_api_endpoint(request: Request):
    data = await request.json()
    global temp
    temp = data.get('temperature')
    print(f'The latest temp equals {temp}')  # For debugging purposes
    # Do something with the data
    return {"message": "Data received successfully"}


frontend.init(app)


if __name__ == '__main__':
    uvicorn.run("server:app", host="0.0.0.0", port=int(os.environ.get('PORT', 8000)), log_level="info")