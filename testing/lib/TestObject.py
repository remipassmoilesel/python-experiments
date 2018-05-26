# -*- coding: utf-8 -*-


class TestObject():

    def sayHello(self):
        print("Hello world !")
        raise Exception("Method is not mocked !")


if __name__ == '__main__':
    testInstance = TestObject()
    testInstance.sayHello()
