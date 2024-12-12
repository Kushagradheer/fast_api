from typing import List
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class TaskBaseSchema(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    priority: int
    due_date:  Optional[datetime] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True


class ListTaskResponse(BaseModel):
    status: str
    results: int
    tasks: List[TaskBaseSchema]