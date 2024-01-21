import os
import sys
from lib.todo_list import ToDoList


class CLIApp:
    def __init__(self):
        self.__todo_list = ToDoList()

    @property
    def todo_list(self):
        return self.__todo_list

    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def get_options_menu():
        str_menu = "1. Ajouter une tâche\n"
        str_menu += "2. Marquer une tâche comme terminée\n"
        str_menu += "3. Afficher la liste des tâches\n"
        str_menu += "4. Quitter"
        return str_menu

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
            print(f'\n{CLIApp.get_options_menu()}')
            choice = input("Choisissez une option (1-4): ")
            CLIApp.clear_screen()

            if choice == "1":
                self.ask_new_task()

            elif choice == "2":
                self.complete_task()

            elif choice == "3":
                self.display_tasks()

            elif choice == "4":
                self.quit()

            else:
                print("Option invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    CLIApp().run()
