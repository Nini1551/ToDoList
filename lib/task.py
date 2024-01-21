class Task:
    def __init__(self, description: str, completed: bool = False):
        self.__description = description
        self.__is_completed = completed

    @property
    def description(self) -> str:
        return self.__description

    @property
    def is_completed(self) -> bool:
        return self.__is_completed

    def __str__(self):
        status = "[x]" if self.is_completed else "[ ]"
        return f"{status} - {self.description}"

    def mark_completed(self):
        self.__is_completed = True
