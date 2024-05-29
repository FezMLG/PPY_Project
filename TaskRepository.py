from sqlite3 import Connection
from typing import List

from task import Task


class TaskRepository:
    def __init__(self, db: Connection):
        self.db: Connection = db

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """)
        self.db.commit()

    def insert(self, task: Task):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO tasks (id, name, description, status, created_at)
            VALUES (?, ?, ?, ?, ?)
            """, (str(task.id), task.name, task.description, task.status.name, task.created_at))
        self.db.commit()

        return task

    def select_all(self, status=None) -> List[Task]:
        cursor = self.db.cursor()

        query = """
            SELECT * FROM tasks
            """

        if status:
            query += f" WHERE status = '{status}'"

        cursor.execute(query)

        tasks = []
        for row in cursor.fetchall():
            task = Task(task_id=row[0], name=row[1], description=row[2], status=row[3], created_at=row[4])
            tasks.append(task)

        return tasks

    def update(self, task: Task):
        cursor = self.db.cursor()
        cursor.execute("""
            UPDATE tasks
            SET name = ?, description = ?, status = ?
            WHERE id = ?
            """, (task.name, task.description, task.status.name, str(task.id))
        )
        self.db.commit()

    def delete(self, task_id: str):
        cursor = self.db.cursor()
        cursor.execute("""
            DELETE FROM tasks
            WHERE id = ?
            """, (task_id,)
                            )
        self.db.commit()

    def select_one_by_id(self, task_id: str):
        cursor = self.db.cursor()
        cursor.execute("""
            SELECT * FROM tasks
            WHERE id = ?
            """, (task_id,)
                            )

        row = cursor.fetchone()
        return Task(task_id=row[0], name=row[1], description=row[2], status=row[3], created_at=row[4])
