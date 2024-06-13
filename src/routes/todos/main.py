from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from exceptions.handler import *

from .models import *
from .controller import *
from .schemas import *


# from auth import *
# from auth.controller import *

# router = APIRouter(
#     prefix="/todos",
#     tags=["todos"],
#     responses={404: {"description": "Not found"}}
#     )

# @router.get("/user")
# async def read_all_by_user(user: dict = Depends(get_db), db: Session = Depends(get_db)):
#     if user is None:
#         raise get_user_exception
#     return db.query(Todos).filter(Todos.owner_id == user.get("id")).all()


# # # get single
# @router.get("/{todo_id}")
# async def read_todos(todo_id: int, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):
#     todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()
#     if todo_model is not None:
#         return todo_model
#     raise http_exception()

# # # create
# @router.post("/")
# async def create_todo(todo: Todo, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):

#     if user is None:
#         raise get_user_exception
    
#     todo_model = Todos()
#     todo_model.title = todo.title
#     todo_model.description = todo.description
#     todo_model.priority = todo.priority
#     todo_model.complete = todo.complete
#     todo_model.owner_id = user.get("id")

#     db.add(todo_model)
#     db.commit()
#     return successful_response(201)


# # update
# @router.put("/{todo_id}")
# async def update_todos(todo_id: int, todo: Todo, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):
    
#     if user is None:
#         raise get_user_exception
    
#     todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()

#     if todo_model is None:
#         raise http_exception()
    
#     todo_model.title = todo.title
#     todo_model.description = todo.description
#     todo_model.priority = todo.priority
#     todo_model.complete = todo.complete

#     db.add(todo_model)
#     db.commit()

#     return successful_response(200)



# # # delete
# @router.delete("/{todo_id}")
# async def delete_todo(todo_id: int, user: dict = Depends(get_db), db: Session = Depends(get_db)):

#     if user is None:
#         raise get_user_exception
    
#     todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get("id")).first()

#     if todo_model is None:
#         raise http_exception()
    
    
#     db.query(Todos).filter(Todos.id == todo_id).delete()
#     db.commit()

#     return successful_response(200)





# import sys
# # sys.path.routerend("..")
# from fastapi import Depends, APIRouter
# from pydantic import BaseModel, Field
# from typing import List, Annotated, Union, Optional
# from .models import *
# from database.database import engine, SessionLocal
# from sqlalchemy.orm import Session
# from .auth import get_user_exception, get_cuurent_user
# from exceptions.handler import *

# router = APIRouter(prefix="/todos", tags=["todos"], responses={404: {"description": "Not found"}})
# models.Base.metadata.create_all(bind=engine)


# class Todo(BaseModel):
#     title: str
#     description: Optional[str]
#     priority: int = Field(gt=0, lt=6, description="The priority must be between 1-5")
#     complete: bool


# def get_db():
#    db = SessionLocal()
#    try:
#        yield db
#    finally:
#        db.close()

# db_dependency = Annotated[Session, Depends(get_db)]


# @router.get("/user")
# async def read_all_by_user(user: dict = Depends(get_db), db: Session = Depends(get_db)):
#     if user is None:
#         raise get_user_exception
#     return db.query(models.Todos).filter(models.Todos.owner_id == user.get("id")).all()


# # # get single
# @router.get("/{todo_id}")
# async def read_todos(todo_id: int, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):
#     todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.get("id")).first()
#     if todo_model is not None:
#         return todo_model
#     raise http_exception()

# # # create
# @router.post("/")
# async def create_todo(todo: Todo, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):

#     if user is None:
#         raise get_user_exception
    
#     todo_model = models.Todos()
#     todo_model.title = todo.title
#     todo_model.description = todo.description
#     todo_model.priority = todo.priority
#     todo_model.complete = todo.complete
#     todo_model.owner_id = user.get("id")

#     db.add(todo_model)
#     db.commit()
#     return successful_response(201)


# # update
# @router.put("/{todo_id}")
# async def update_todos(todo_id: int, todo: Todo, user: dict = Depends(get_cuurent_user), db: Session = Depends(get_db)):
    
#     if user is None:
#         raise get_user_exception
    
#     todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.get("id")).first()

#     if todo_model is None:
#         raise http_exception()
    
#     todo_model.title = todo.title
#     todo_model.description = todo.description
#     todo_model.priority = todo.priority
#     todo_model.complete = todo.complete

#     db.add(todo_model)
#     db.commit()

#     return successful_response(200)



# # # delete
# @router.delete("/{todo_id}")
# async def delete_todo(todo_id: int, user: dict = Depends(get_db), db: Session = Depends(get_db)):

#     if user is None:
#         raise get_user_exception
    
#     todo_model = db.query(models.Todos).filter(models.Todos.id == todo_id).filter(models.Todos.owner_id == user.get("id")).first()

#     if todo_model is None:
#         raise http_exception()
    
    
#     db.query(models.Todos).filter(models.Todos.id == todo_id).delete()
#     db.commit()

#     return successful_response(200)