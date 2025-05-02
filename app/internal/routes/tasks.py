"""Routers for CRUD of tasks levels."""

from typing import List

from dependency_injector.wiring import Provide, inject
from fastapi import Depends, status

from app.internal.routes import tasks_router
from app.pkg import models


@tasks_router.get(
    "/",
    response_model=List[models.Tasks],
    status_code=status.HTTP_200_OK,
    description="Get all tasks",
)
@inject
async def read_all_tasks():
    pass