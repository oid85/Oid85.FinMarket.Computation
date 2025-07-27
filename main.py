import uvicorn
from fastapi import FastAPI, Body
import adf

app = FastAPI()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1102, reload=True)


@app.post("/api/is-stationary")
def is_stationary(data=Body()):
    result = adf.is_stationary(data["data"])
    return {"result": result}
