"""Models fot tasks."""


from typing import Optional
from datetime import datetime, timedelta

from pydantic.fields import Field
from pydantic.types import PositiveInt
from pydantic import validator

from app.pkg.models.base import BaseModel
from app.pkg.models.validators.tasks import is_correct_data_finish, is_status_in_enum


__all__ = [
    "Tasks",
    "TaskLevelFields",
    "CreateTasksCommand",
    "UpdateTasksCommand",
    "ReadTasksQuery",
    "DeleteTasksCommand"
]


FROM_TIME = (
    datetime.now() + timedelta(minutes=10)
).timestamp()
TO_TIME = (
    datetime.now() + timedelta(hours=1)
).timestamp()


class BaseTaskLevel(BaseModel):
    """Base model for tasks levels."""


class TaskLevelFields:
    """Model fields of tasks"""

    id: PositiveInt = Field(description="Internal task id.", example=1)
    title: str = Field(description="Task name.", example="Start coding")
    description: Optional[str] = Field(
        None,
        description="Task description.",
        example="Today I want to code",
    )
    data_create: Optional[float] = Field(
        None,
        description="Task creation date.",
        example=FROM_TIME
    )
    data_finish: float = Field(description="Task finish date.", example=TO_TIME)
    status: str = Field("pending", description="Task status.", example="pending")


class _Tasks(BaseTaskLevel):
    data_finish: float = TaskLevelFields.data_finish
    title: str = TaskLevelFields.title
    description: Optional[str] = TaskLevelFields.description
    status: str = TaskLevelFields.status


class _TasksCommand(_Tasks):
    @validator("data_finish")
    def validate_data_finish(cls, value):
        return is_correct_data_finish(value)
    
    @validator("status")
    def validate_status(cls, value):
        return is_status_in_enum(value)


class Tasks(_Tasks):
    id: PositiveInt = TaskLevelFields.id
    data_create: float = TaskLevelFields.data_create


# Commands
class CreateTasksCommand(_TasksCommand):
    ...


class UpdateTasksCommand(_TasksCommand):
    id: PositiveInt = TaskLevelFields.id


class DeleteTasksCommand(BaseTaskLevel):
    id: PositiveInt = TaskLevelFields.id


# Queries
class ReadTasksQuery(BaseTaskLevel):
    id: PositiveInt = TaskLevelFields.id
