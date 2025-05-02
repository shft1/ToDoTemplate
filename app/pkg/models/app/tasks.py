"""Models fot tasks."""

from typing import Optional
from datetime import datetime, timedelta
from pydantic.fields import Field
from pydantic.types import PositiveInt
from pydantic import validators

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
).isoformat(timespec='minutes')
TO_TIME = (
    datetime.now() + timedelta(hours=1)
).isoformat(timespec='minutes')


class BaseTaskLevel(BaseModel):
    """Base model for tasks levels."""


class TaskLevelFields:
    """Model fields of tasks"""

    id: PositiveInt = Field(description="Internal task id.", example=1)
    title: str = Field(max_length=100, description="Task name.", example="Start coding")
    description: Optional[str] = Field(
        None,
        description="Task description.",
        example="Today I want to code",
    )
    data_create: Optional[datetime] = Field(
        None,
        description="Task creation date.",
        example=FROM_TIME
)
    data_finish: datetime = Field(
        description="Task finish date.",
        example=TO_TIME
    )
    status: str = Field("pending", description="Task status.", example="pending")


class _Tasks(BaseTaskLevel):
    title: str = TaskLevelFields.title
    description: Optional[str] = TaskLevelFields.description


class _TasksCommand(_Tasks):
    data_finish: datetime = TaskLevelFields.data_finish
    status: str = TaskLevelFields.status

    @validators("data_finish")
    def validate_data_finish(cls, value):
        return is_correct_data_finish(value)
    
    @validators("status")
    def validate_status(cls, value):
        return is_status_in_enum(value)


class Tasks(_Tasks):
    id: PositiveInt = TaskLevelFields.id
    data_create: datetime = TaskLevelFields.data_create
    data_finish: datetime = TaskLevelFields.data_finish


# Commands
class CreateTasksCommand(_TasksCommand):
    ...


class UpdateTasksCommand(_TasksCommand):
    ...


class DeleteTasksCommand(BaseTaskLevel):
    id: PositiveInt = TaskLevelFields.id


# Queries
class ReadTasksQuery(BaseTaskLevel):
    id: PositiveInt = TaskLevelFields.id
