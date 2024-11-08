from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import RedirectResponse

from train.app.configuration.SecurityConfig import verification
from train.app.configuration.database import get_db
from train.app.schema.Item import ItemCreate
from train.app.service import crud

router = APIRouter(
    prefix="",
    tags=["items"],
)

@router.get("/hello")
async def root(authentication = Depends(verification)):
    print(authentication)
    return RedirectResponse(url="/items")


@router.get("/items")
async def get_items(db: Session = Depends(get_db)):
    items = crud.get_items(db)
    return items

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
