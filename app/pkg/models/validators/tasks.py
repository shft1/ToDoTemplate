"""Validators for tasks model."""

from app.pkg.models.base import BaseEnum
from datetime import datetime
from typing import Optional


class Status(str, BaseEnum):
    PENDING = "pending"
    PROCESS = "process"
    READY = "ready"


def is_correct_data_finish(value: Optional[datetime]):
    if value and value < datetime.now():
        raise ValueError(
            f"Дата окончания задачи {value} не может быть раньше текущей!"
        )
    return value


def is_status_in_enum(value: Optional[str]):
    if value and value not in Status:
        raise ValueError(
            f"Статус {value} должен быть равен "
            f"одному из следующих значений: "
            f"pending, process, ready"
        )
    return value