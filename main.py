from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

stopFlag = 1

app = FastAPI()


class StartNumber(BaseModel):
    startNum: int


@app.get("/checkFlag")
async def check_flag():
    return JSONResponse(content=jsonable_encoder({"Flag": stopFlag}))


@app.post("/start")
async def start(start_num: StartNumber):
    global stopFlag
    stopFlag = 0
    print(start_num.startNum)
    return JSONResponse(content={"message": f"started with num = {start_num.startNum}"})


@app.get("/stop")
async def root():
    global stopFlag
    stopFlag = 1
    return JSONResponse(content={"message": 'stopped'})


if __name__ == '__main__':
    print("Start program")
