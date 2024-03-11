from Src.Logics.convertor import convertor
from Src.reference import reference
from Src.Logics.datetime_convertor import datetime_convertor
from Src.Logics.basic_convertor import basic_convertor
from datetime import datetime


class reference_convertor(convertor):
    __maps = {}

    def __map(self):

        self.__maps[str] = basic_convertor
        self.__maps[datetime] = datetime_convertor
        self.__maps[int] = basic_convertor
        self.__maps[float] = basic_convertor
        self.__maps[bool] = basic_convertor

        for inheritor in reference.__subclasses__():
            self.__maps[inheritor] = reference_convertor

    def convert(self, object: reference):
        """
            Конвертор Reference
        """
        super().get_fields(object)
        self.__map()
        res = {}
        fields = self.fields
        for field in fields:
            k = False
            field_data = getattr(object, field)
            for i in self.__maps:
                if isinstance(field_data, i):
                    _converter = self.__maps[i]()
                    res[field] = _converter.convert(field_data)
                    k = True
                    break
            if not k:
                res[field] = field_data

        return res
