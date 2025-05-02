"""Exceptions for Tasks model."""

from starlette import status

from app.pkg.models.base import BaseAPIException


class TaskNotFound(BaseAPIException):
    status_code = status.HTTP_404_NOT_FOUND
    message = "Такой задачи не существует!"
