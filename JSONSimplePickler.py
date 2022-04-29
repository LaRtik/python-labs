import json
from SimplePickler import SimplePickler


class JSONSerializer(SimplePickler):
    @classmethod
    def format(cls, obj_dict):
        return obj_dict

    @classmethod
    def restore(cls, obj_dict_formatted):
        return obj_dict_formatted
