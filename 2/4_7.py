from fastapi import FastAPI

app = FastAPI()
country_dict = {
    'Russia': ['Moscow', 'St. Petersburg', 'Novosibirsk', 'Ekaterinburg', 'Kazan'],
    'USA': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia'],
}
@app.get("/country/{country}")
async def last_cities(country:str,limit:int) ->dict:
    return {"country":country,"cities":country_dict[country][:limit]}