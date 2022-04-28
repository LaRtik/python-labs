import inspect
import pickle
import json


def dump(obj: object):
    return inspect.getmembers(obj)


def hello():
    print("Hello World")


if __name__ == '__main__':
    test = {
        "name": "blablalba",
        "surname:": "blaz",
        "dict": (1, 2, 3)
    }
    a = int(42)
    print(type(a))
    s = "Hello World"
    l = [a, s]
    print(dump(a))
    print(hello.__code__.co_name)
    print(pickle.dumps(a))
    print(pickle.loads(pickle.dumps(a)))
    print(json.dumps(l))
    print('Hello World')
