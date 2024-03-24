from Src.Logics.convertor import convertor
from datetime import datetime


class datetime_convertor(convertor):
    @staticmethod
    def convert(object: datetime):
        """
            Корвертор дат
        """
        return {
            'year': object.year,
            'month': object.month,
            'day': object.day,
            'hour': object.hour,
            'minute': object.minute,
            'second': object.second,
            'microsecond': object.microsecond
        }
