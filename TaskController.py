from TaskStatusEnum import TaskStatus
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

        selected_task = self.show_and_select_task(tasks, controller)

        return self.view_task(selected_task, controller)

    def view_task(self, task: Task, controller):
        controller.print_header(f"Task: {task.name}")

        print(f"""
        Name: {task.name}
        Description: {task.description}
        Status: {task.status}
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

    def edit_task(self, task: Task, controller):
        controller.print_header(f"Edit: {task.name}")

        name = input(f"Name ({task.name}): ")
        description = input(f"Description ({task.description}): ")

        print("Select status:")
        for status in TaskStatus:
            print(f"{status.value}. {status.name}")

        new_status: int | None = controller.get_input_int(f"Status ({task.status}): ")

        if name == "":
            name = task.name

        if description == "":
            description = task.description

        if new_status is None:
            pass
        elif new_status > len(TaskStatus) or new_status < 0:
            print("Invalid status, not updating status")
        else:
            print("Updating status")
            task.set_status(TaskStatus(new_status))

        task.set_name(name)
        task.set_description(description)

        print(task)

        self.task_service.update_task(task)

        print("Task updated")

        self.view_task(task, controller)

    def delete_task(self, task, controller):
        controller.print_header(f"Delete: {task.name}")

        self.task_service.remove_task(str(task.id))

        print("Task deleted")

        self.view_tasks(controller)

    def view_tasks_by_status(self, controller):
        controller.print_header("View Tasks by Status")

        print("Select status:")
        for status in TaskStatus:
            print(f"{status.value}. {status.name}")

        selected_status: int | None = controller.get_input_int("Status: ")

        if selected_status is None or selected_status > len(TaskStatus) or selected_status < 0:
            print("Invalid status")
            return self.view_tasks_by_status(controller)

        tasks = self.task_service.get_all_tasks(TaskStatus(selected_status))

        controller.print_header(f"Tasks with status: {TaskStatus(selected_status).name}")

        selected_task = self.show_and_select_task(tasks, controller)

        return self.view_task(selected_task, controller)

    def search_tasks_by_name(self, controller):
        controller.print_header("Search Tasks by Name")

        name = input("Enter name: ")

        tasks = self.task_service.find_by_name(name)

        controller.print_header(f"Tasks with name: {name}")

        selected_task = self.show_and_select_task(tasks, controller)

        return self.view_task(selected_task, controller)

    def show_and_select_task(self, tasks, controller):
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
                return self.show_and_select_task(tasks, controller)
            else:
                return tasks[int(option) - 1]
