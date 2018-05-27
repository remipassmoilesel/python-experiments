# -*- coding: utf-8 -*-


class TestObject():

    def sayHello(self):
        print("Hello world !")
        raise Exception("Method is not mocked !")

    def sayHelloTo(self, name):
        print("Hello " + name + " !")
        raise Exception("Method is not mocked !")

