from fastapi import FastAPI 


app = FastAPI()

@app.get('/')
async def model_endpoint():
    return {"hello":"Wrold"}
    