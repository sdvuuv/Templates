from Src.reference import reference


#
# Типы событий
#
class logging_type(reference):

    @staticmethod
    def debug() -> str:
        """
            Категория DEBUG
        Returns:
            str: _description_
        """
        return "DEBUG"

    @staticmethod
    def info() -> str:
        """
            Категория INFO
        Returns:
            str: _description_
        """
        return "INFO"

    @staticmethod
    def error() -> str:
        """
            Категория ERROR
        Returns:
            str: _description_
        """
        return "ERROR"
