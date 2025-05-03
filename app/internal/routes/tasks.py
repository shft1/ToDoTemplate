"""Routers for CRUD of tasks levels."""

from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, status

from app.internal.routes import tasks_router
from app.internal.services import Services
from app.internal.services.tasks import TaskService
from app.pkg import models


@tasks_router.get(
    "/",
    response_model=List[models.Tasks],
    status_code=status.HTTP_200_OK,
    description="Get all tasks",
)
@inject
async def read_all_tasks(
    task_service: TaskService = Depends(Provide[Services.task_service])
):
    return await task_service.read_all_tasks()


@tasks_router.get(
    "/{task_id:int}/",
    response_model=models.Tasks,
    status_code=status.HTTP_200_OK,
    description="Read specific task"
)
@inject
async def read_task(
    task_id: int,
    task_service: TaskService = Depends(Provide[Services.task_service])
):
    return await task_service.read_task(query=models.ReadTasksQuery(id=task_id))


@tasks_router.post(
    "/",
    response_model=models.Tasks,
    status_code=status.HTTP_201_CREATED,
    description="Create task"
)
@inject
async def create_task(
    cmd: models.CreateTasksCommand,
    task_service: TaskService = Depends(Provide[Services.task_service])
):
    return await task_service.create_task(cmd=cmd)


@tasks_router.patch(
    "/{task_id:int}",
    response_model=models.Tasks,
    status_code=status.HTTP_200_OK,
    description="Update task"
)
@inject
async def update_task(
    task_id: int,
    cmd: models.UpdateTasksCommand,
    task_service: TaskService = Depends(Provide[Services.task_service])
):
    return await task_service.update_task(id=task_id, cmd=cmd)


@tasks_router.delete(
    "/{task_id:int}/",
    response_model=models.Tasks,
    status_code=status.HTTP_204_NO_CONTENT,
    description="Delete task"
)
@inject
async def delete_task(
    task_id: int,
    task_service: TaskService = Depends(Provide[Services.task_service])
):
    return await task_service.delete_task(cmd=models.DeleteTasksCommand(id=task_id))
