import os
from lib.todo_list import ToDoList

class CLIApp:
    def __init__(self):
        self.__todo_list = ToDoList()

    @property
    def todo_list(self):
        return self.__todo_list

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        while True:
            print("\n1. Ajouter une tâche")
            print("2. Marquer une tâche comme terminée")
            print("3. Afficher la liste des tâches")
            print("4. Quitter")

            choice = input("Choisissez une option (1-4): ")
            self.clear_screen()

            if choice == "1":
                description = input("Entrez la description de la tâche: ")
                self.todo_list.add_task(description)

            elif choice == "2":
                try:
                    print(f"\n{self.todo_list.get_uncompleted_str_tasks()}\n")
                    index = int(input("Entrez l'index de la tâche terminée: ")) - 1
                    self.todo_list.mark_task_completed(index)
                except ValueError as error:
                    print(error)

            elif choice == "3":
                print(f"\n{self.todo_list.get_str_tasks()}")

            elif choice == "4":
                break

            else:
                print("Option invalide. Veuillez choisir une option valide.")


if __name__ == "__main__":
    CLIApp().run()
