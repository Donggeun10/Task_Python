from typing import List

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status

from train.app.configuration.SecurityConfig import verification, validate_token
from train.app.configuration.database import get_db
from train.app.schema.Item import ItemCreate, Item
from train.app.service import crud

router = APIRouter(
    prefix="/api",
    tags=["items"],
)

@router.get("/hello")
async def root(authentication = Depends(verification)):
    if authentication:
        return "hello world"


@router.get("/items", response_model=List[Item])
async def get_items(db: Session = Depends(get_db), authentication = Depends(verification)):
    if authentication:
        return crud.get_items(db)


# Protected, get items route
@router.get('/item/sample', response_model=Item)
def read_items(valid: bool = Depends(validate_token)):
    if valid :
        return Item.model_validate({'id': 1, 'name': 'red ball', 'description': 'A red ball', 'price': 100})
    else:
        raise HTTPException(status_code=401, detail="Invalid Token")

@router.post("/item",
             status_code=status.HTTP_201_CREATED,
             responses={
                 201: {
                     "content": {"application/json": {}},
                     "description": "member is properly inserted",
                 }
             })
async def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    db_item = crud.create_item(db, item)
    if db_item is None:
        raise HTTPException(status_code=500, detail="item("+db_item.name+") is not properly inserted")

    return {"result":"member("+db_item.name+") is properly inserted"}
