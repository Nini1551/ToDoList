import os
from lib.to_do_list import ToDoList


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\n1. Ajouter une tâche")
        print("2. Marquer une tâche comme terminée")
        print("3. Afficher la liste des tâches")
        print("4. Quitter")

        choice = input("Choisissez une option (1-4): ")
        clear_screen()

        if choice == "1":
            description = input("Entrez la description de la tâche: ")
            todo_list.add_task(description)

        elif choice == "2":
            try:
                print(f"\n{todo_list.get_tasks()}\n")
                index = int(input("Entrez l'index de la tâche terminée: ")) - 1
                todo_list.mark_task_completed(index)
            except ValueError as error:
                print(error)

        elif choice == "3":
            print(f"\n{todo_list.get_tasks()}")

        elif choice == "4":
            break

        else:
            print("Option invalide. Veuillez choisir une option valide.")
