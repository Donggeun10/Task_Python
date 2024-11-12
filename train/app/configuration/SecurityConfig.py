# FastAPI Imports
import logging
from functools import lru_cache

import httpx
from cachetools.func import ttl_cache
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials, HTTPBearer, \
    HTTPAuthorizationCredentials
from starlette.config import Config

from train.app.configuration.LoggingConfig import stream_handler, file_handler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


basic_security = HTTPBasic()

users = {
    "robot": {
        "password": "play",
        "token": "",
        "privileged": True
    }
}

# User Verification Function
def verification(creds: HTTPBasicCredentials = Depends(basic_security)):
    username = creds.username
    password = creds.password
    if validate_user_info(username, password):
        return True
    else:
        # From FastAPI
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

@lru_cache(ttl_cache(maxsize=64, ttl=60))
def validate_user_info(username: str, password: str):
    if username in users and password == users[username]["password"]:
        logger.debug("User is validated")
        return True
    else:
        return False

bearer_security = HTTPBearer()
config = Config('train/.env.local')

def validate_token(authorization: HTTPAuthorizationCredentials = Depends(
    bearer_security)):

    res = validate_remotely(
        authorization.credentials,
        config('OKTA_ISSUER'),
        config('OKTA_CLIENT_ID'),
        config('OKTA_CLIENT_SECRET')
    )

    if bool(res):
        return True
    else:
        # From FastAPI
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Inactive Token",
            headers={"WWW-Authenticate": "Bearer Token"},
        )

@lru_cache(ttl_cache(maxsize=64, ttl=60))
def validate_remotely(token, issuer, client_id, client_secret):

    headers = {
        'accept': 'application/json',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
    }
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'token': token,
    }
    url = issuer + '/oauth2/v1/introspect'

    response = httpx.post(url, headers=headers, data=data)

    logger.debug(response.status_code)
    logger.debug(str(response.json()))
    return response.status_code == httpx.codes.OK and response.json()['active']