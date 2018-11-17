#!/usr/bin/env python3.6

import os


def main():
    currentVenv: str = os.getenv('VIRTUAL_ENV')
    print("Hello world !")
    print("Using virtual environment: " + currentVenv)


if __name__ == '__main__':
    main()
