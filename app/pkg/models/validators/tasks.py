"""Validators for tasks model."""


from typing import Optional
from datetime import datetime

from app.pkg.models.base import BaseEnum


class Status(str, BaseEnum):
    PENDING = "pending"
    PROCESS = "process"
    READY = "ready"


def is_correct_data_finish(value: Optional[float]):
    if value and datetime.fromtimestamp(value) < datetime.now():
        raise ValueError(
            f"Дата окончания задачи {value} не может быть раньше текущей!"
        )
    return value


def is_status_in_enum(value: Optional[str]):
    if value and value not in (status.value for status in Status):
        raise ValueError(
            f"Статус {value} должен быть равен "
            f"одному из следующих значений: "
            f"pending, process, ready"
        )
    return value