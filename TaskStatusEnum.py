from enum import Enum


class TaskStatus(Enum):
    TODO = 1
    IN_PROGRESS = 2
    COMPLETED = 3

    def __str__(self):
        return self.name
