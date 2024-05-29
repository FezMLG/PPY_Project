from TaskRepository import TaskRepository
from task import Task


class TaskService:

    def __init__(self, task_repository: TaskRepository):
        self.task_repository: TaskRepository = task_repository

    def create_task(self, task: Task):
        self.task_repository.insert(task)

    def get_all_tasks(self):
        return self.task_repository.select_all()
