from fastapi import FastAPI,Path

app = FastAPI()
@app.get("/category/{category_id}/products")
async def category(page:int,category_id:int=Path(gt=0,description="Category ID")) ->dict:
    return {'category_id':category_id,"page":page}