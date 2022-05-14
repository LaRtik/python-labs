import inspect
import math
import pickle
import json

from serializers.PicklerFactory import PicklerCreator

c = 42
test_global = 42


def hello():
    print("Hello World")


def f(x):
    a = 123
    print(a)
    return math.sin(x * a * c)


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

    print(type(a))
    s = "Hello World"
    l = [a, s]
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
    d = "ez 4 G2"
    json_pickler = PicklerCreator.create("json")
    formatted = json_pickler.pre_dumps(d)
    unformatted = json_pickler.post_loads(formatted)
    print(unformatted)


def test_butoma():
    yaml_pickler = PicklerCreator.create("yaml")
    formatted = yaml_pickler.dumps(f)
    unformatted = yaml_pickler.loads(formatted)
    print(unformatted(12))

def test_butoma_file():
    json_pickler = PicklerCreator.create("json")
    file = open("formatted.json", "w")
    json_pickler.dump(file, f)
    file.close()
    file = open('formatted.json', "r")
    unformatted = json_pickler.load(file)
    print(unformatted(12))


def test_simple_class():
    yaml_pickler = PicklerCreator.create("yaml")
    formatted = yaml_pickler.dumps(TestClass)
    unformatted = yaml_pickler.loads(formatted)
    unformatted.say_my_name(unformatted)


if __name__ == '__main__':
    test_butoma_file()
    test_butoma()
    test_simple_class()

    # formatted = JSONSerializer.dumps(test_prim)
    # #file = open("formatted.json", 'w')
    # #print(JSONSerializer.dump(file, test_prim))
    # loaded = JSONSerializer.loads(formatted)

    # formattedTOML = TOMLSerializer.dumps(test_prim)
    # loadedTOML = TOMLSerializer.loads(formattedTOML)
    # loadedTOML()

    # formattedYAML = YAMLSerializer.dumps(test_prim)
    # loadedYAML = YAMLSerializer.loads(formattedYAML)
    # loadedYAML()
