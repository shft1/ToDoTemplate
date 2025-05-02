"""
tasks
"""

from yoyo import step

__depends__ = {'20231112_04_IxuQN-directions', '20231112_05_knHgl-cities', '20231112_06_vK6vZ-contacts'}

steps = [
    step(
        """
        create table if not exists tasks (
            id serial primary key,
            title varchar(100) not null,
            description text,
            data_create timestamp default now(),
            data_finish timestamp not null,
            status varchar(20) default 'pending' not null 
        );
        """,
        """
            drop table if exists tasks cascade;
        """
    )
]
