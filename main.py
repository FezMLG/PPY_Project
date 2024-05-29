import sqlite3

from Controller import Controller
from TaskController import TaskController
from TaskRepository import TaskRepository
from TaskService import TaskService

db_connection = sqlite3.connect("todo.sqlite")


task_repository = TaskRepository(db_connection)
task_service = TaskService(task_repository)
task_controller = TaskController(task_service)

controller = Controller(task_controller)

task_repository.create_table()

while True:
    controller.main_menu()
