from sqlite3 import Connection
from typing import List

from task import Task


class TaskRepository:
    def __init__(self, db: Connection):
        self.db: Connection = db
        self.cursor = self.db.cursor()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        self.db.commit()

    def insert(self, task: Task):
        self.cursor.execute(
            """
            INSERT INTO tasks (id, name, description, status, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (str(task.id), task.name, task.description, str(task.status), task.created_at)
        )
        self.db.commit()

    def select_all(self) -> List[Task]:
        self.cursor.execute(
            """
            SELECT * FROM tasks
            """
        )
        tasks = []
        for row in self.cursor.fetchall():
            task = Task(
                task_id=row[0],
                name=row[1],
                description=row[2],
                status=row[3],
                created_at=row[4]
            )
            tasks.append(task)
        return tasks

