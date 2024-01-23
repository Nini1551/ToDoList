from typing import Callable

class Option:
    def __init__(self, lib: str, func: Callable):
        self.__lib = lib
        self.__func = func

    @property
    def lib(self):
        return self.__lib

    def __str__(self):
        return f'{self.lib}'

    def execute(self,*args,**kwargs):
        self.__func(*args,**kwargs)
