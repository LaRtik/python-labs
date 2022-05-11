import json
import types

from SimplePickler import SimplePickler


class JSONSerializer(SimplePickler):

    @classmethod
    def format(cls, obj):
        result = ""
        if isinstance(obj, dict):
            result += "{"
            for key, value in obj.items():
                #key = key.replace('"', '\\"')
                result += f'"{key}": {cls.format(value)},'
            if result[-1] == ',':
                result = result[:-1]
            result += '}'
            return result
        elif isinstance(obj, tuple):
            result += "["
            for el in obj:
                result += f'{cls.format(el)},'
            if result[-1] == ',':
                result = result[:-1]
            result += ']'
            return result
        elif isinstance(obj, str):
            obj = obj.replace('"', '\\"')
            if obj == 'formatted':
                print("formatted")
            return f'"{obj}"'
        elif isinstance(obj, bytes):
            return int.from_bytes(obj, "big")
        elif isinstance(obj, bool):
            return str(obj).lower()
        elif obj is None:
            return "null"
        else:
            return str(obj)


    @classmethod
    def restore(cls, obj_dict_formatted):
        return obj_dict_formatted
