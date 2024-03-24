
from Src.reference import reference
from Src.exceptions import exception_proxy, argument_exception
from Src.Models import storage_model
from Src.Models import nomenclature_model
from Src.Models import unit_model
from Src.Models import storage_type_model
from datetime import datetime
#
# Модель склада
#


class storage_transaction_model(reference):

    # Тип операции
    __operaton_type: str = ""

    # Количество
    __quantity: int = ""

    # Склад, над которым проводится операция
    __storage: storage_model = None

    # Номенклатура
    __nomenclature: nomenclature_model = None

    # Единица измерения
    __unit: unit_model = None

    # Период транзакции
    __period: datetime = None

    def __init__(self, name: str):
        super().__init__(name)

    @property
    def storage(self) -> storage_model:
        """
            Склад на котором проводится операция
        Returns:
            _type_: _description_
        """
        return self.__storage

    @storage.setter
    def storage(self, storage: storage_model):
        self.__storage = storage

    @property
    def operation_type(self) -> str:
        """
            Тип операции
        Returns:
            _type_: _description_
        """
        return self.__operaton_type

    @operation_type.setter
    def operation_type(self, operation_type: storage_type_model):
        self.__operaton_type = operation_type

    @property
    def quantity(self) -> int:
        """
            Количество
        Returns:
            _type_: _description_
        """
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int):
        exception_proxy.validate(quantity, int)
        if quantity == 0:
            raise argument_exception(
                "Невозможно провести транзакцию нуля элементов")
        self.__quantity = quantity

    @property
    def unit(self) -> unit_model:
        """
            Единица измерения
        Returns:
            _type_: _description_
        """
        return self.__unit

    @unit.setter
    def unit(self, unit: unit_model):
        self.__unit = unit_model

    @property
    def nomenclature(self) -> nomenclature_model:
        """
            Номенклатура
        Returns:
            _type_: _description_
        """
        return self.__nomenclature

    @nomenclature.setter
    def nomenclature(self, nomenclature: nomenclature_model):
        self.__nomenclature = nomenclature

    @property
    def period(self) -> datetime:
        """
            Дата транзакции
        Returns:
            _type_: _description_
        """
        return self.__period

    @period.setter
    def period(self, period: datetime):
        self.__period = period
