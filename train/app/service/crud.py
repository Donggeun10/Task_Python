import logging

from sqlalchemy.orm import Session

from train.app.configuration.LoggingConfig import log
from train.app.entity.Item import Item
from train.app.schema.Item import ItemCreate

logger = logging.getLogger(__name__)
logger.parent = log

def get_items(db: Session):
    return db.query(Item).all()

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()

def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, item: Item, updated_item: ItemCreate):
    for key, value in updated_item.model_dump().items():
        setattr(item, key, value)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item: Item):
    db.delete(item)
    db.commit()

db : Session
def set_db_session(db_session : Session):
    global db
    db = db_session


