from sqlite3 import Connection

from task import Task


class TaskRepository:
    def __init__(self, db: Connection):
        self.db: Connection = db

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute(
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
        cursor = self.db.cursor()
        cursor.execute(
            """
            INSERT INTO tasks (id, name, description, status, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (str(task.id), task.name, task.description, task.status, task.created_at)
        )
        self.db.commit()

    def select_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM tasks")
        return cursor.fetchall()
