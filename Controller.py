from TaskController import TaskController


class Controller:
    options = []

    def __init__(self, task_controller: TaskController):
        self.task_controller = task_controller

    def print_header(self, header: str):
        print("")
        print(f"########## {header} ##########")
        print("")

    def main_menu(self):
        self.print_header("Main Menu")
        print("""
        1. Create Task
        2. View Tasks
        
        0. Exit
        """)
        option = input("Enter option: ")

        if option == "1":
            self.task_controller.create_task()
        elif option == "2":
            self.task_controller.view_tasks(self)
        elif option == "0":
            exit(0)
