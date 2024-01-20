import os


class Task:
    def __init__(self, description: str, completed: bool = False):
        self.__description = description
        self.__completed = completed

    @property
    def description(self) -> str:
        return self.__description

    @property
    def completed(self) -> bool:
        return self.__completed

    def __str__(self):
        status = "[x]" if self.completed else "[ ]"
        return f"{status} - {self.description}"

    def mark_completed(self):
        self.__completed = True


class ToDoList:
    def __init__(self):
        self.__tasks = []

    @property
    def tasks(self) -> list[Task]:
        return self.__tasks

    def add_task(self, description: str):
        task = Task(description)
        self.tasks.append(task)

    def mark_task_completed(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
        else:
            raise ValueError("Index invalide ! ")

    def get_tasks(self) -> str:
        if not self.tasks:
            return "Aucune tâche dans la liste."

        str_tasks = 'To Do List :\n'
        for i, task in enumerate(self.tasks):
            str_tasks += f"{i + 1}. {task}\n"
        return str_tasks[:-1]


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
