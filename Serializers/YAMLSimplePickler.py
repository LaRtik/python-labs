from SimplePickler import SimplePickler
from yaml import load, dump, Loader

class YAMLSerializer(SimplePickler):
    @classmethod
    def format(cls, obj):
        test = dump(obj)
        print(test)
        return dump(obj)

    @classmethod
    def restore(cls, obj):
        return load(obj, Loader=Loader)
