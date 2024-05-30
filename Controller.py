from TaskController import TaskController


class Controller:
    options = {}

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
        3. View Tasks by Status
        4. Search Tasks by Name
        
        0. Exit
        """)
        option = input("Enter option: ")

        if option == "1":
            self.task_controller.create_task()
        elif option == "2":
            self.task_controller.view_tasks(self)
        elif option == "3":
            self.task_controller.view_tasks_by_status(self)
        elif option == "4":
            self.task_controller.search_tasks_by_name(self)
        elif option == "0":
            exit(0)

    def get_input_int(self, message: str) -> int | None:
        inp = input(message)
        try:
            if inp == "":
                return None
            return int(inp)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return self.get_input_int(message)

