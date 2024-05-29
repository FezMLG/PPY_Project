import datetime
import uuid

import TaskStatusEnum


class Task:
    def __init__(self, name: str, description: str, status: TaskStatusEnum):
        self.id: uuid.UUID = uuid.uuid4()
        self.name: str = name
        self.description: str = description
        self.status: str = status
        self.created_at: datetime = datetime.datetime.now()

    def __str__(self):
        return f"{self.name} - {self.description} - {self.status}"
