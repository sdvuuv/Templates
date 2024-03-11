from abc import ABC, abstractmethod
from Src.reference import reference
from datetime import datetime


class convertor(ABC):
    __fields = None

    @property
    def fields(self):
        return self.__fields

    def get_fields(self, object):
        self.__fields = list(filter(lambda x: not x.startswith(
            "_") and not x.startswith("create_"), dir(object)))
        return self.fields

    @abstractmethod
    def convert(self, object) -> dict:
        pass
