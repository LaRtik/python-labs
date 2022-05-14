from SimplePickler import SimplePickler
import toml

class TOMLSerializer(SimplePickler):
    @classmethod
    def format(cls, obj):
        test = toml.dumps(obj)
        print(test)
        return toml.dumps(obj)

    @classmethod
    def restore(cls, obj):
        return toml.loads(obj)
