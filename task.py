import datetime
import uuid

import TaskStatusEnum


class Task:
    def __init__(self, name: str, description: str, status: TaskStatusEnum, task_id: uuid.UUID = uuid.uuid4(),
                 created_at: datetime = datetime.datetime.now()):
        self.id: uuid.UUID = task_id
        self.name: str = name
        self.description: str = description
        self.status: str = status
        self.created_at: datetime = created_at

    def __str__(self):
        return (f"Task(id={self.id}, name={self.name}, description={self.description}, status={self.status}, "
                f"created_at={self.created_at})")

    def set_name(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")

        self.name = name

    def set_description(self, description):
        self.description = description

    def set_status(self, status):
        self.status = status
