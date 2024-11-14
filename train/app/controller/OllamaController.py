import logging

from fastapi import APIRouter
from fastapi.params import Depends

from train.app.configuration.LoggingConfig import log
from train.app.configuration.SecurityConfig import verification
from train.app.service.ollamaService import get_ollama_joke, \
    get_spring_boot_version, summarize

logger = logging.getLogger(__name__)
logger.parent = log

router = APIRouter(
    prefix="/api/ollama",
    tags=["ollama"],
)

@router.get("/hello")
async def root(authentication = Depends(verification)):
    logger.debug("hello")
    if authentication:
        return "hello world"


@router.post("/joke")
async def joke(authentication = Depends(verification), keyword: str = None):
    if authentication:
        return get_ollama_joke(keyword)


@router.post("/query")
async def query(authentication = Depends(verification), log_file: str = None):
    if authentication:
        return get_spring_boot_version(log_file)

@router.post("/query/stacktrace")
async def query_stacktrace(authentication = Depends(verification), log_file: str = None, stack_trace_file: str = None):
    if authentication:
        return summarize(log_file, stack_trace_file)