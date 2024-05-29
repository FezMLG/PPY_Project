import TaskStatusEnum
from TaskService import TaskService
from task import Task


class TaskController:
    def __init__(self, task_service: TaskService):
        self.task_service = task_service

    def create_task(self):
        print("Create Task")
        name = input("Name: ")
        description = input("Description: ")

        task = Task(name, description)
        created = self.task_service.create_task(task)

        print(f"Task created: {created}")

    def view_tasks(self, controller):
        controller.print_header("View Tasks")

        tasks = self.task_service.get_all_tasks()

        i = 0
        for task in tasks:
            i += 1
            print(f"{i}. {task.name} - {task.status}")

        print("")
        print("0. Back")

        option = input("Enter option: ")
        if option == "0":
            controller.main_menu()
        else:
            if int(option) > len(tasks) or int(option) - 1 < 0:
                print("Invalid option")
                self.view_tasks(controller)
            else:
                self.view_task(tasks[int(option) - 1], controller)

    def view_task(self, task: Task, controller):
        controller.print_header(f"Task: {task.name}")

        print(f"""
        Name: {task.name}
        Description: {task.description}
        Status: {task.status.name}
        Created At: {task.created_at}
        """)

        print("""
        1. Edit Task
        2. Delete Task
        
        0. Back
        """)

        option = input("Enter option: ")
        if option == "0":
            self.view_tasks(controller)
        elif option == "1":
            self.edit_task(task, controller)
        elif option == "2":
            self.delete_task(task, controller)
        else:
            print("Invalid option")
            self.view_task(task, controller)

    def edit_task(self, task, controller):
        controller.print_header(f"Edit: {task.name}")

        name = input(f"Name ({task.name}): ")
        description = input(f"Description ({task.description}): ")

        print("Select status:")
        for status in TaskStatusEnum.TaskStatus:
            print(f"{status.value}. {status.name}")
        status = input(f"Status ({task.status}): ")

        if name == "":
            name = task.name

        if description == "":
            description = task.description

        if status == "":
            status = task.status

        task.set_name(name)
        task.set_description(description)
        task.set_status(TaskStatusEnum.TaskStatus(int(status)))

        self.task_service.update_task(task)

        print("Task updated")

        self.view_task(task, controller)

    def delete_task(self, task, controller):
        controller.print_header(f"Delete: {task.name}")

        self.task_service.remove_task(str(task.id))

        print("Task deleted")

        self.view_tasks(controller)

