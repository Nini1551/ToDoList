import os
import sys
from lib.todo_list import ToDoList
from lib.menu import Menu


class CLIApp:
    def __init__(self):
        self.__todo_list = ToDoList()
        self.__menu = Menu()
        self.__init_menu()

    @property
    def todo_list(self):
        return self.__todo_list

    @property
    def menu(self):
        return self.__menu

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init_menu(self):
        self.menu.add_option('Ajouter une tâche', self.ask_new_task)
        self.menu.add_option('Marquer une tâche comme terminée', self.complete_task)
        self.menu.add_option('Afficher la liste des tâches', self.display_tasks)
        self.menu.add_option('Quitter', self.quit)

    def ask_new_task(self):
        description = input("Entrez la description de la tâche: ")
        self.todo_list.add_task(description)

    def complete_task(self):
        try:
            print(f"\n{self.todo_list.get_uncompleted_str_tasks()}\n")
            index = int(input("Entrez l'index de la tâche terminée: ")) - 1
            self.todo_list.mark_task_completed(index)
        except ValueError as error:
            print(error)

    def display_tasks(self):
        print(f"\n{self.todo_list.get_str_tasks()}")

    def quit(self):
        sys.exit()

    def run(self):
        while True:
            print(f'\n{self.menu.get_menu_options()}')
            index_choice = int(input("Choisissez une option (1-4): ")) - 1
            CLIApp.clear_screen()

            try:
                self.menu.execute_option(index_choice)
            except IndexError as error:
                print(error)


if __name__ == "__main__":
    CLIApp().run()
