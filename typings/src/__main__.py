#!/usr/bin/env python3

# -*- coding: utf-8 -*-
from . import TypedObject

if __name__ == '__main__':
    testInstance = TypedObject()

    # Wrong type arguments throw
    # returnValue = testInstance.sayHelloTo(1)
    returnValue = testInstance.sayHelloTo('Mary')

    # But wrong return type not
    print(returnValue)

    # Wrong affectation too
    maybeInteger: list = 0
    print(maybeInteger)
