from . import schemas, models
from sqlalchemy.orm import Session
from fastapi import Depends , HTTPException , status , APIRouter , Response
from .database import get_db
from typing import Optional
from datetime import datetime


router = APIRouter(tags=["Tasks"])


# Get all records
@router.get('/', response_model=schemas.ListTaskResponse)
def get_tasks(
    db: Session = Depends(get_db),
    limit: int = 10, 
    page: int = 1,
    search: str = '',
    priority: Optional[int] = None,
    overdue : Optional[bool]= None
    ):
    try:
        skip = (page - 1) * limit

        
        query = db.query(models.Task).filter(models.Task.title.contains(search))


        if priority:
            query = query.filter(models.Task.priority == priority)

        if overdue is not None:
            current_time = datetime.now()
            if overdue:
                query = query.filter(models.Task.due_date < current_time)

            else:
                query = query.filter((models.Task.due_date >= current_time) | (models.Task.due_date == None))
        
        tasks = query.limit(limit).offset(skip).all()

        return {
            'status' :'success',
            'results' : len(tasks),
            'tasks' : tasks
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# Add new Task
@router.post('/', response_model=schemas.TaskBaseSchema)
def create_task(task: schemas.TaskBaseSchema, db: Session = Depends(get_db)):
    ## WE can also add Input check limit ( like adding limit for task priority value)
    
    try:
        new_task = models.Task(**task.model_dump(exclude_unset=True))
        
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        
        return new_task
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))



#Get Task with ID
@router.get('/{task_id}', response_model=schemas.TaskBaseSchema)
def get_task(task_id: int, db: Session = Depends(get_db)):

    try:

        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        return task
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#Put/ Update Task
@router.put('/{task_id}', response_model=schemas.TaskBaseSchema)
def update_task(task_id: int, task_update: schemas.TaskBaseSchema, db: Session = Depends(get_db)):
    
    ## WE can add Input check limit also (same as above for priority value)

    try:
        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        update_data = task_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task, key, value)
        
        db.commit()
        db.refresh(task)
        
        return task
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

#Delete Task
@router.delete('/{task_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    
    try:
        task = db.query(models.Task).filter(models.Task.id == task_id).first()
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        db.delete(task)
        db.commit()
        
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))