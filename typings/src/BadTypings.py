from . import Square
from . import TypedObject


class BadTypings:

    def start(self) -> None:
        testInstance = TypedObject()

        # Type checking does not affect runtime
        testInstance.sayHelloTo(1)
        testInstance.sayHelloTo('Mary')

        # Wrong affectation does not throw
        maybeInteger: list = 0
        print(maybeInteger)

        # Wrong list content does not throw
        testInstance.useStringList(['string', 'list'])
        testInstance.useStringList([0, 1])

        # Wrong list content does not throw
        squareInstance = Square(5)
        testInstance.useSquare(squareInstance)
        testInstance.useSquare(['string', 'list'])
