"""Service for manage tasks"""

from app.pkg import models
from app.internal.repository.postgresql import tasks
from app.internal.repository.repository import BaseRepository

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
     