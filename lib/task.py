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
