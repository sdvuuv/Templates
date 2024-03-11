from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.reference_convert import reference_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.reference import reference
from datetime import datetime
from Src.exceptions import operation_exception


class convert_factory:
    __maps = {}

    def __init__(self) -> None:
        self.__build_structure()

    def __build_structure(self):
        """
            Формирование структуры    
        """
        self.__maps[int] = basic_convertor
        self.__maps[float] = basic_convertor
        self.__maps[bool] = basic_convertor
        self.__maps[str] = basic_convertor
        self.__maps[datetime] = datetime_convertor
        for inheritor in reference.__subclasses__():
            self.__maps[inheritor] = reference_convertor

    """
        Фабричный метод
    """

    def convert(self, object) -> dict:
        obj = None
        if object is None:
            return ""

        if len(self.__maps) == 0:
            self.__build_structure()

        for key in self.__maps.keys():
            if isinstance(object, key):
                obj = self.__maps[key]

        if obj is None:
            raise operation_exception(f"Для {type(object)} не существует конвертора.")

        convertor = obj()

        res = convertor.convert(object)

        return res
