from Src.Logics.reporting import reporting
from Src.exceptions import operation_exception
from Src.Logics.convert_factory import convert_factory
from Src.Logics.convertor import convertor
import json


class json_reporting(reporting):
    __convert_factory = convert_factory()

    def create(self, typeKey: str):
        """
            Сформировать отчет из json    
        """
        super().create(typeKey)
        result = []

        items = self.data[typeKey]

        if items == None:
            raise operation_exception(
                "Невозможно сформировать данные. Данные не заполнены")

        if len(items) == 0:
            raise operation_exception(
                "Невозможно сформировать данные. Нет данных!")

        data = {}
        for item in items:
            for field in self.fields:
                value = getattr(item, field)
                value = self.__convert_factory.convert(value)
                data[field] = value
            result.append(data)

        data = json.dumps(result)
        return data
