"""Repository for tasks"""


from typing import List

from app.pkg import models
from app.internal.repository.postgresql.connection import get_connection
from app.internal.repository.repository import Repository
from app.internal.repository.postgresql.handlers.collect_response import (
    collect_response,
)


__all__ = ["TaskRepository"]


class TaskRepository(Repository):
    """Task repository implementation"""

    @collect_response
    async def read(self, query: models.ReadTasksQuery) -> models.Tasks:
        q = """
            select
                *
            from tasks
            where id = %(id)s
        """
        async with get_connection() as cur:
            await cur.execute(q, query.to_dict())
            return await cur.fetchone()
        

    @collect_response
    async def read_all(self, by_timeline, by_status) -> List[models.Tasks]:
        q = """
            select
                *
            from tasks
        """
        if by_timeline and by_status:
            q += " order by (data_finish - data_create), status"
        elif by_timeline:
            q += " order by (data_finish - data_create)"
        elif by_status:
            q += " order by status"

        async with get_connection() as cur:
            await cur.execute(q)
            return await cur.fetchall()
        
    
    @collect_response
    async def create(self, cmd: models.CreateTasksCommand) -> models.Tasks:
        q = """
            insert into tasks(
                title, description, data_finish, status
            ) values (
                %(title)s, %(description)s, %(data_finish)s, %(status)s
            )
            returning *
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()


    @collect_response
    async def update(self, cmd: models.UpdateTasksCommand) -> models.Tasks:
        q = """
            update tasks
            set
                title = coalesce(%(title)s, title),
                description = coalesce(%(description)s, description),
                data_finish = coalesce(%(data_finish)s, data_finish),
                status = coalesce(%(status)s, status)
            where id = %(id)s
            returning *;
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()

    
    @collect_response
    async def delete(self, cmd: models.DeleteTasksCommand) -> models.Tasks:
        q = """
            delete from tasks
            where id = %(id)s
            returning *
        """
        async with get_connection() as cur:
            await cur.execute(q, cmd.to_dict())
            return await cur.fetchone()
