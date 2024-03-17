from Src.Models.unit_model import unit_model
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Storage.storage import storage
from Src.Logics.report_factory import report_factory
import unittest
from Src.Models.group_model import group_model
from Src.Models.nomenclature_model import nomenclature_model
from Src.Logics.convertor import convertor
from Src.Logics.convert_factory import convert_factory
from Src.Logics.basic_convertor import basic_convertor
from Src.Logics.reference_convert import reference_convertor
from Src.Logics.datetime_convertor import datetime_convertor
from Src.Logics.process_factory import process_factory

import unittest

#
# Набор автотестов для проверки работы фабричного метода
#


class factory_test(unittest.TestCase):
    def test_check_create_receipts(self):
        # Подготовка
        items = start_factory.create_receipts()

        # Действие

        # Проверки
        assert len(items) > 0

    #
    # Проверка создание начальной номенклатуры
    #
    def test_check_create_nomenclatures(self):
        # Подготовка
        items = start_factory.create_nomenclatures()

        # действие

        # Прверки
        assert len(items) > 0

    #
    # Проверка создание списка единиц измерения
    #

    def test_check_create_units(self):
        # Подготовка
        items = start_factory.create_units()

        # Действие

        # Проверки
        assert len(items) > 0

    #
    # Проверка создания списка групп
    #
    def test_check_create_groups(self):
        # Подготовка
        items = start_factory.create_groups()

        # Действие

        # Проверки
        assert len(items) > 0

    #
    # Проверка работы класса start_factory. Метод create
    #

    def test_check_factory_create(self):
        # Подготовка
        manager = settings_manager()
        factory = start_factory(manager.settings)

        # Действие
        result = factory.create()

        # Проверка
        if manager.settings.is_first_start == True:
            assert result == True
            assert not factory.storage is None
            assert storage.nomenclature_key in factory.storage.data
            assert storage.receipt_key in factory.storage.data
            assert storage.group_key in factory.storage.data
            assert storage.unit_key in factory.storage.data
        else:
            assert result == False
    # Можно ли без принтов как то сделать???
    def test_check_transactions_create(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        result = factory.create_transaction()

        print(result)

        assert result != None
        assert len(result) == 20
        assert result[12].nomenclature.unit != None
        #print(result)

    def test_check_turn_calculation(self):
        manager = settings_manager()
        factory = start_factory(manager.settings)

        transactions_list = factory.create_transaction()
        result = process_factory.process_storage_turn(transactions_list)
        #for item in result:
        #    print(item.quantity, item.nomenclature.name, item.storage.name)
        assert result != None
        assert len(result) <= 20
        assert len(result) > 0
