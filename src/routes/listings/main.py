# import sys
# sys.path.routerend("..")
from fastapi import Depends, APIRouter
from pydantic import BaseModel, Field
from typing import List, Annotated, Union, Optional
from passlib.context import CryptContext
from config.database import engine, SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from exceptions.handler import *
from config.config import Settings

from .models import *
from .controller import *
from .schemas import *
from src.routes.auth.controller import get_cuurent_user

# router = APIRouter(
#     prefix="/listings",
#     tags=["listings"],
#     responses={404: {"description": "Not found"}}
#     )


# # # get all
# @router.get("/")
# async def read_all(db: Session = Depends(get_db)):
#     listing_model = db.query(Listings).all()
#     return listing_model


# @router.get("/user")
# async def read_all_by_user(user: dict = Depends(get_db), db: Session = Depends(get_db)):
#     if user is None:
#         raise get_user_exception
#     return db.query(Listings).filter(Listings.owner_id == user.get("id")).all()


# # # get single
# @router.get("/{listing_id}")
# async def read_Listings(listing_id: int, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):
#     listing_model = db.query(Listings).filter(Listings.id == listing_id).filter(Listings.owner_id == user.get("id")).first()
#     if listing_model is not None:
#         return listing_model
#     raise http_exception()

# # # create
# @router.post("/")
# async def create_listing(listing: Listing, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):

#     if user is None:
#         raise get_user_exception
    
#     listing_model = Listings()
#     listing_model.title = listing.title
#     listing_model.description = listing.description
#     listing_model.company = listing.company
#     listing_model.logo = listing.logo
#     listing_model.tags = listing.location
#     listing_model.email = listing.email
#     listing_model.owner_id = user.get("id")

#     db.add(listing_model)
#     db.commit()
#     return successful_response(201)


# # update
# @router.put("/{listing_id}")
# async def update_Listings(listing_id: int, listing: Listing, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):
    
#     if user is None:
#         raise get_user_exception
    
#     listing_model = db.query(Listings).filter(Listings.id == listing_id).filter(Listings.owner_id == user.get("id")).first()

#     if listing_model is None:
#         raise http_exception()
    
#     listing_model.title = listing.title
#     listing_model.description = listing.description
#     listing_model.company = listing.company
#     listing_model.logo = listing.logo
#     listing_model.tags = listing.location
#     listing_model.email = listing.email

#     db.add(listing_model)
#     db.commit()

#     return successful_response(200)



# # # delete
# @router.delete("/{listing_id}")
# async def delete_listing(listing_id: int, user: dict = Depends(get_db), db: Session = Depends(get_db)):

#     if user is None:
#         raise get_user_exception
    
#     listing_model = db.query(Listings).filter(Listings.id == listing_id).filter(Listings.owner_id == user.get("id")).first()

#     if listing_model is None:
#         raise http_exception()
    
    
#     db.query(Listings).filter(Listings.id == listing_id).delete()
#     db.commit()

#     return successful_response(200)



















# import sys
# # sys.path.routerend("..")
# from fastapi import Depends, APIRouter
# from pydantic import BaseModel
# from typing import List, Annotated, Union, Optional
# from .models import *
# from database.database import engine, SessionLocal
# from sqlalchemy.orm import Session
# from .auth import get_user_exception, get_cuurent_user
# from exceptions.handler import *

# router = APIRouter(prefix="/listings", tags=["listings"], responses={404: {"description": "Not found"}})
# models.Base.metadata.create_all(bind=engine)


# class Listing(BaseModel):
#     title: str
#     company: str
#     location: str
#     description: str
#     logo: str
#     tags: str
#     email: str
#     # timestamp: str

# def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

# db_dependency = Annotated[Session, Depends(get_db)]


# # # get all
# @router.get("/")
# async def read_all(db: Session = Depends(get_db)):
#     listing_model = db.query(models.Listings).all()
#     return listing_model


# @router.get("/user")
# async def read_all_by_user(user: dict = Depends(get_db), db: Session = Depends(get_db)):
#     if user is None:
#         raise get_user_exception
#     return db.query(models.Listings).filter(models.Listings.owner_id == user.get("id")).all()


# # # get single
# @router.get("/{listing_id}")
# async def read_Listings(listing_id: int, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):
#     listing_model = db.query(models.Listings).filter(models.Listings.id == listing_id).filter(models.Listings.owner_id == user.get("id")).first()
#     if listing_model is not None:
#         return listing_model
#     raise http_exception()

# # # create
# @router.post("/")
# async def create_listing(listing: Listing, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):

#     if user is None:
#         raise get_user_exception
    
#     listing_model = models.Listings()
#     listing_model.title = listing.title
#     listing_model.description = listing.description
#     listing_model.company = listing.company
#     listing_model.logo = listing.logo
#     listing_model.tags = listing.location
#     listing_model.email = listing.email
#     listing_model.owner_id = user.get("id")

#     db.add(listing_model)
#     db.commit()
#     return successful_response(201)


# # update
# @router.put("/{listing_id}")
# async def update_Listings(listing_id: int, listing: Listing, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):
    
#     if user is None:
#         raise get_user_exception
    
#     listing_model = db.query(models.Listings).filter(models.Listings.id == listing_id).filter(models.Listings.owner_id == user.get("id")).first()

#     if listing_model is None:
#         raise http_exception()
    
#     listing_model.title = listing.title
#     listing_model.description = listing.description
#     listing_model.company = listing.company
#     listing_model.logo = listing.logo
#     listing_model.tags = listing.location
#     listing_model.email = listing.email

#     db.add(listing_model)
#     db.commit()

#     return successful_response(200)



# # # delete
# @router.delete("/{listing_id}")
# async def delete_listing(listing_id: int, user: dict = Depends(get_db), db: Session = Depends(get_db)):

#     if user is None:
#         raise get_user_exception
    
#     listing_model = db.query(models.Listings).filter(models.Listings.id == listing_id).filter(models.Listings.owner_id == user.get("id")).first()

#     if listing_model is None:
#         raise http_exception()
    
    
#     db.query(models.Listings).filter(models.Listings.id == listing_id).delete()
#     db.commit()

#     return successful_response(200)