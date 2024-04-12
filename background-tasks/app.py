from fastapi import FastAPI, BackgroundTasks, status
from core.models import Message
from core.notification import notify
from asyncio import sleep


app = FastAPI()


@app.post("/", status_code = status.HTTP_200_OK, response_model=dict)
async def read_task(message: Message, task: BackgroundTasks):

    task.add_task(schedule_task, message.title, message.body)

    return {"task status": "scheduled"}


async def schedule_task(title: str, body: str):

    await sleep(5)  # wait for 5 seconds

    notify(title, body)