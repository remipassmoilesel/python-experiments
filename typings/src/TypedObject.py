# -*- coding: utf-8 -*-

from typing import List
from . import Square


class TypedObject():

    def sayHelloTo(self, name: str) -> str:
        hello = "Hello " + str(name) + " !"
        print(hello)
        return hello

    def useStringList(self, list: List[str]):
        print(list)

    def useSquare(self, square: Square):
        print(square)
