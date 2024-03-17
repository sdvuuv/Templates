from Src.reference import reference
from Src.exceptions import exception_proxy, argument_exception
from datetime import datetime


#
# Модель склада
#
class storage_model(reference):

    # Адрес склада
    __storage_location: str = ""

    # Место для доп свойств

    def __init__(self, name: str, location: str = ""):

        if location != "":
            self.__storage_location = location

        super().__init__(name)

    @property
    def location(self) -> str:
        """
            Адрес склада
        Returns:
            _type_: _description_
        """
        return self.__storage_location

    @location.setter
    def location(self, location: str):
        exception_proxy.validate(location, str)
        self.__storage_location = location
