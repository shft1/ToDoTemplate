"""Service for manage tasks"""


import typing

from app.pkg import models
from app.internal.repository.postgresql import tasks
from app.internal.repository.repository import BaseRepository
from app.pkg.models.exceptions.repository import EmptyResult
from app.pkg.models.exceptions.tasks import TaskNotFound


__all__ = ["TaskService"]


class TaskService:
    """Service for manage tasks"""

    #: TaskRepository: TaskRepository repository implementation.
    repository: tasks.TaskRepository

    def __init__(self, task_repository: BaseRepository):
        self.repository = task_repository

    async def create_task(self, cmd: models.CreateTasksCommand) -> models.Tasks:
        """Create task

        Args:
            cmd: CreateTasksCommand command

        Returns:
            Tasks: Created task
        """
        return await self.repository.create(cmd=cmd)

    async def read_task(self, query: models.ReadTasksQuery) -> models.Tasks:
        """Read task

        Args:
            query: ReadTasksQuery query
        
        Returns:
            Tasks: Read task
        """ 
        try:
            return await self.repository.read(query=query)
        except EmptyResult as e:
            raise TaskNotFound from e

    async def read_all_tasks(self) -> typing.List[models.Tasks]:
        """Read all tasks

        Returns:
            List[Tasks]: Read all tasks
        """
        try:
            return await self.repository.read_all()
        except EmptyResult as e:
            raise TaskNotFound from e

    async def update_task(self, id: int, cmd: models.UpdateTasksCommand) -> models.Tasks:
        """Update task
        
        Args:
            cmd: UpdateTasksCommand command
        
        Returns:
            Tasks: Updated task
        """
        return await self.repository.update(id=id, cmd=cmd)

    async def delete_task(self, cmd: models.DeleteTasksCommand) -> models.Tasks:
        """Delete task

        Args:
            cmd: DeleteTasksCommand command
        """
        return await self.repository.delete(cmd=cmd)
