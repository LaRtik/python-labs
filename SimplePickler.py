from abc import ABC, abstractmethod
import inspect


class Serializer(ABC):
    def dumps(self, obj: object):
        if inspect.isclass(obj):
            pass
        if inspect.ismethod(obj):
            pass
        else:
            return self.format(obj)

    @abstractmethod
    def format(self):
        pass
