from typing import List
from fastapi import Body, FastAPI, status, Header
from pydantic import BaseModel, Field


app = FastAPI()

bearer = 'Bearer 123kljksji-3sfas'


class Product(BaseModel):
  barcode: List = Field(...)
  sortingLane: List = Field(...)
  receivingLane: str = Field(...)


@app.get(
  path='/users',
  status_code=status.HTTP_200_OK
)
def sorting_lane(
  Authorization: str = Header(
    description='Bearer {API Token}'
  ),
  product: Product = Body()
):
  if Authorization == bearer:
    if '1ZR000000000004753' in product.barcode:
      return {
        "assignedLane": 1,
        "laneLightStatus": [
          { "1": 1 },
          { "2": 0 },
          { "3": 1 },
          { "4": 0 },
          { "5": 1 },
          { "6": 0 },
          { "7": 1 },
          { "8": 0 },
          { "9": 1 },
          { "10": 0 },
          { "11": 1 },
          { "12": 0 }
        ]
      }
    else:
      return { 
        "error": [
          { "message": "issue found" }
        ]
      }
  else:
    return {
      "error": {
        "message": "Authentication information is missing or invalid"
      }
    }
