from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
import db
import os


stopFlag = 1

app = FastAPI()
app.middleware(
    CORSMiddleware
)


class StartNumber(BaseModel):
    startNum: int


@app.get("/checkFlag")
async def checkFlag():
    return JSONResponse(content=jsonable_encoder({"Flag": stopFlag}))


@app.post("/start")
async def start(start_num: StartNumber):
    global stopFlag
    stopFlag = 0
    db.insertLog(start_num.startNum)
    os.system("start cmd /k python robot.py " + str(start_num.startNum))
    return JSONResponse(content={"message": f"started with num={start_num.startNum}"})


@app.get("/stop")
async def stop():
    global stopFlag
    stopFlag = 1
    db.updateEndTime()
    return JSONResponse(content={"message": 'stopped'})


@app.get("/logs")
async def logs():
    select = "SELECT * FROM logs"
    res = db.cursor.execute(select)
    prepared_logs = map(db.prepareData, res.fetchall())
    return JSONResponse(content=jsonable_encoder(list(prepared_logs)))


if __name__ == '__main__':
    print("Start program")
