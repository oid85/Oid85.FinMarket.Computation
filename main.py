from fastapi import FastAPI, Body
import utils

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Oid85.FinMarket.Computation"}

@app.post("/api/series-is-stationary")
def series_is_stationary(data  = Body()):
    series = data["series"]
    result = utils.series_is_stationary(series)
    return { "result": result }
