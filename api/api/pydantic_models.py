from datetime import datetime
from pydantic import (
    BaseModel,
    Field,
)


class RecordID(BaseModel):
    id: str = Field(..., alias="_id")

    class Config:
        allow_population_by_field_name = True


class RecordIn(BaseModel):
    timestamp: int
    value1: str
    value2: float
    value3: bool


class RecordOut(BaseModel):
    id: str = Field(..., alias="_id")
    timestamp: int
    value1: str
    value2: float
    value3: bool

    class Config:
        allow_population_by_field_name = True


class RecordInDB(RecordOut):
    creationDate: int
    lastModificationDate: int
