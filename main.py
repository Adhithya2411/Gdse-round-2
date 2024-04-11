import argparse
from tabulate import tabulate



class Task:
    def __init__(self, name, status, assignee, reporter, priority):
        self.name = name
        self.status = status
        self.assignee = assignee
        self.reporter = reporter
        self.priority = priority


class BoardsMenu:
    def __init__(self):
        self.boards = []
        with open("adhi.txt", 'a+') as f:
            f.seek(0)
            data = f.readlines()

        for x in data:
            self.boards.append(x.rstrip("\n"))

    def add_board(self, board):
        self.boards.append(board)
        for i in range(len(self.boards)):
            self.boards[i] = self.boards[i] + "\n"
        with open("adhi.txt", 'w') as f1:
            f1.writelines(self.boards)

    def remove_board(self, board_name):
        for i in range(len(self.boards)):
            if self.boards[i] == board_name:
                self.boards.remove(self.boards[i])

                for i in range(len(self.boards)):
                    self.boards[i] = self.boards[i] + "\n"
                with open("adhi.txt", 'w') as f1:
                    f1.writelines(self.boards)
                return True
        return False

    def all_boards(self):
        with open("adhi.txt", 'a+') as f2:
            f2.seek(0)
            data = f2.readlines()
            for x in data:
                print(x.rstrip("\n"))

    def active_board(self, board_name):

        for boar in self.boards:

            if boar == board_name:
                boarder(board_name)
                return True
        return False


def show_menu():
    options = ['1.Add a board', '2.Delete a board', '3.Show the available boards', '4.Activate the board',
               '5.Quit']
    for option in options:
        print(option)
    opt = int(input("Enter the option you would like to choose:"))

    if opt == 1:
        board_name = input("Enter the name of the board:")
        BoardsMenu().add_board(board_name)

    if opt == 2:
        remove_board = input("Enter the name of the board to be removed:")
        BoardsMenu().remove_board(remove_board)

    if opt == 3:
        BoardsMenu().all_boards()
    if opt == 4:
        name = input("Enter the name of the board to activate:")
        BoardsMenu().active_board(name)

    if opt == 5:
        print("Exitting!")
        return "quit"


class KanbanBoard:
    def __init__(self, name):
        self.name = name
        self.tasks = {'Todo': [], 'In Progress': [], 'Done': []}

    def add_task(self, task):
        self.tasks[task.status].append(task)


    def show_board(self):
        print(f"Kanban Board: {self.name}")
        for status in self.tasks:
            print("\n" + "=" * 40)
            print(f"{status}:")
            if self.tasks[status]:
                headers = ['Task', 'Assignee', 'Reporter', 'Priority']
                table_data = []
                for task in self.tasks[status]:
                    table_data.append([task.name, task.assignee, task.reporter, task.priority])
                print(tabulate(table_data, headers=headers, tablefmt="grid"))
            else:
                print("No tasks")




def boardmenu():
    parser_start = argparse.ArgumentParser(description="CLI Kanban Board")
    parser_start.add_argument('--name', type=str, help="Initiate", required=True)
    args = parser_start.parse_args()

    if args.name == "1234":
        show_menu()
        if show_menu() == "quit":
            return "end"


def boarder(board):
    while True:
        print("\n{}".format("=" * 50))
        print("Kanban board:{}".format(board))
        print("=" * 50)

        board = KanbanBoard(board)


        print("\nCommands:")
        print("1. Add task")
        print("2. Move task")
        print("3. Remove task")
        print("4. Show the task by priority")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter task name: ")
            status = input("Enter task status (Todo/In Progress/Done): ")
            assignee = input("Enter task assignee: ")
            reporter = input("Enter task reporter: ")
            priority = input("Enter task priority (High/Medium/Low): ")
            task = Task(name, status, assignee, reporter, priority)
            KanbanBoard(board).add_task(task)
        elif choice == '2':
            task_name = input("Enter task name: ")
            new_status = input("Enter new status (Todo/In Progress/Done): ")
            if not board.move_task(task_name, new_status):
                print("Task not found!")
        elif choice == '3':
            task_name = input("Enter task name: ")
            if not board.remove_task(task_name):
                print("Task not found!")

        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


def main():
    while True:
        print("Menu")
        boardmenu()
        if boardmenu() == "end":
            break


if __name__ == "__main__":
    main()
