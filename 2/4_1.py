from fastapi import FastAPI

app = FastAPI()

@app.get("/product/{id}")
async def detail_view(id:int) ->dict:
    return{"product":f"Stock number {id}"}