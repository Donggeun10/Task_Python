import logging
import sys
import time
from contextlib import asynccontextmanager

import uvicorn
from fastapi import (FastAPI, Depends, Request)
from fastapi.responses import RedirectResponse

from train.app.configuration.LoggingConfig import stream_handler, \
    file_handler
from train.app.configuration.SecurityConfig import verification
from train.app.configuration.database import create_tables
from train.app.controller import ItemController

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # When service starts.
    create_tables()
    logger.info("Service started.")
    yield

    # When service is stopped.
    # shutdown()
    logger.info("Service stopped.")

app = FastAPI(lifespan=lifespan)

app.include_router(ItemController.router)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = round((time.time() - start_time) * 1000)
    response.headers["X-Process-Time-ms"] = str(process_time)

    return response

@app.get("/")
async def root(authentication = Depends(verification)):
    if authentication:
        return RedirectResponse(url="/api/hello")


def serve(args):
    uvicorn.run(app, host="0.0.0.0", port=int(args[2]),
                reload=False,
                workers=1)

if __name__ == "__main__":
    serve(sys.argv)