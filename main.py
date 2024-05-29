import sqlite3

from TaskStatusEnum import TaskStatus
from TaskRepository import TaskRepository
from TaskService import TaskService
from task import Task

db_connection = sqlite3.connect("todo.sqlite")

task_repository = TaskRepository(db_connection)

task_repository.create_table()

task_service = TaskService(task_repository)

task = Task(
    name="Task 1",
    description="Description 1",
    status=TaskStatus.TODO
)

# task_service.create_task(task)
print(task_service.get_all_tasks(TaskStatus.IN_PROGRESS))
