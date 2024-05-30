from TaskRepository import TaskRepository
from task import Task


class TaskService:

    def __init__(self, task_repository: TaskRepository):
        self.task_repository: TaskRepository = task_repository

    def create_task(self, task: Task):
        return self.task_repository.insert(task)

    def get_all_tasks(self, status=None):
        return self.task_repository.select_all(status)

    def update_task(self, task: Task):
        self.task_repository.update(task)

    def remove_task(self, task_id: str):
        self.task_repository.delete(task_id)

    def get_task(self, task_id: str):
        return self.task_repository.select_one_by_id(task_id)

    def find_by_name(self, name):
        return self.task_repository.select_by_name(name)
