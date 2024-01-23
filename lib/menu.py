from typing import Callable
from .option import Option


class Menu:
    def __init__(self, title: None|str = None):
        self.__title = title
        self.__options = []

    @property
    def title(self):
        return self.__title

    def add_option(self, lib: str, func: Callable):
        self.__options.append(Option(lib, func))

    def execute_option(self, index: int, *args, **kwargs):
        if 0 <= index < len(self.__options):
            self.__options[index].execute(*args, **kwargs)
        else:
            raise IndexError("Option invalide. Veuillez choisir une option valide.")

    def get_menu_options(self) -> str:
        menu = f'{self.title}\n\n' if self.title else ''
        for index, option in enumerate(self.__options):
            menu += f'{index+1}. {option}\n'
        return menu[:-1]
