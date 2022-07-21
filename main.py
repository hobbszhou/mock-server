import json
import uvicorn
from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.openapi import constants
from starlette.requests import Request
from starlette.responses import JSONResponse

router = APIRouter()

with open('mock.json', encoding="utf-8") as f:
    data = json.loads(f.read())


def f(r: Request):
    path = r.url.path
    if path in data:
        return JSONResponse(data[path])
    raise HTTPException(status_code=404, detail="接口不存在")


for k in data:
    router.add_route(k, f, methods=constants.METHODS_WITH_BODY)

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':

    uvicorn.run(app="main:app", host="0.0.0.0", port=8901, reload=True)
