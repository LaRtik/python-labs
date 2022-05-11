import inspect
import math
import pickle
import json
from pprint import pprint

import JSONSimplePickler
from JSONSimplePickler import JSONSerializer


def dump(obj: object):
    return inspect.getmembers(obj)


def hello():
    print("Hello World")


test_global = 42


class TestClass:
    name = "Volodya"
    surname = "Badboy"
    age = 66

    def say_my_name(self):
        print(f"My name is {self.name} {self.surname}")

    def random_number(self):
        print(test_global + self.age)


def test_prim():
    test = {
        "name": "blablalba",
        "surname:": "blaz",
        "dict": (1, 2, 3)
    }
    a = 42
    b = "hello"
    c = True
    d = 42.42
    print(dump(a))
    print(dump(b))
    print(dump(c))
    print(dump(d))

    print(type(a))
    s = "Hello World"
    l = [a, s]
    print(dump(a))
    print(hello.__code__.co_name)
    print(pickle.dumps(a))
    print(pickle.loads(pickle.dumps(a)))
    print(json.dumps(l))
    print('Hello World')
    a = int(5)
    print(inspect.isclass(a))
    print(a)


def test_primitives():
    a = 42
    b = 42.42
    c = True
    d = "hello wrotebal"
    formatted = JSONSerializer.pre_dumps(d)
    unformatted = JSONSerializer.loads(formatted)
    print(unformatted)


def sums(a, b):
    return a + b


def test_globals(a, b, c):
    return math.sin(sums(a, b) * c)


def test_func():
    test = {
        "name": "blablalba",
        "surname:": "blaz",
        "dict": (1, 2, 3)
    }
    formatted = JSONSerializer.pre_dumps(test_globals)
    print(test_globals(1, 2, 3))
    print(JSONSerializer.loads(formatted)(1, 2, 3))


if __name__ == '__main__':
    formatted = JSONSerializer.dumps(test_prim)
    file = open("formatted.json", 'w')
    print(JSONSerializer.dump(file, test_prim))
    # loaded = JSONSerializer.loads(formatted)
    print()
