from Src.Logics.convertor import convertor


class basic_convertor(convertor):
    @staticmethod
    def convert(object):
        """
            Конвертер базовый
        """
        return {"value": object}
