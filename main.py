import inspect
import pickle
import json
from pprint import pprint

import JSONSimplePickler
from JSONSimplePickler import JSONSerializer


def dump(obj: object):
    return inspect.getmembers(obj)


def hello():
    print("Hello World")


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
    formatted = JSONSerializer.dumps(d)
    unformatted = JSONSerializer.loads(formatted)
    print(unformatted)


if __name__ == '__main__':
    test = {
        "name": "blablalba",
        "surname:": "blaz",
        "dict": (1, 2, 3)
    }
    print(JSONSerializer.dumps(test_primitives))
