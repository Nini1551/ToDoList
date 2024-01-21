from .task import Task


class ToDoList:
    def __init__(self):
        self.__tasks = []

    @property
    def tasks(self) -> list[Task]:
        return self.__tasks

    def add_task(self, description: str):
        task = Task(description)
        self.tasks.append(task)
        self.sort()

    def mark_task_completed(self, index: int):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_completed()
            self.sort()
        else:
            raise ValueError("Index invalide ! ")

    def sort(self):
        self.tasks.sort(key=lambda task: task.completed)

    def has_uncompleted_task(self) -> bool:
        return any(map(lambda task: not task.completed, self.tasks))

    def get_uncompleted_tasks(self):
        uncompleted_todo_list = ToDoList()
        for task in self.tasks:
            if task.completed:
                break
            uncompleted_todo_list.add_task(task.description)
        return uncompleted_todo_list

    def get_str_tasks(self) -> str:
        if not self.tasks:
            return "Aucune tâche dans la liste."

        str_tasks = 'To Do List :\n'
        for i, task in enumerate(self.tasks):
            str_tasks += f"{i + 1}. {task}\n"
        return str_tasks[:-1]

    def get_uncompleted_str_tasks(self) -> str:
        if not self.has_uncompleted_task():
            return "Toutes les tâches sont terminées."

        uncompleted_todo_list = self.get_uncompleted_tasks()
        return uncompleted_todo_list.get_str_tasks()
