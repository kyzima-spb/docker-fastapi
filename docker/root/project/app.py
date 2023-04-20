from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pythoninfo import pythoninfo


app = FastAPI()


@app.get('/', response_class=HTMLResponse)
async def index():
    return pythoninfo()
