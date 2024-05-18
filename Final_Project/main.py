from fastapi import FastAPI, HTTPException, status, Query, Response
from pydantic import BaseModel
from typing import Optional
from random import randrange
from database import *
from routes import router



app = FastAPI()



app.include_router(router, prefix="/book", tags=["book"])