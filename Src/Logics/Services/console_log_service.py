from Src.Logics.Services.service import service
from Src.Models.event_type import event_type
from Src.Storage.storage import storage
from Src.errors import error_proxy
from Src.exceptions import exception_proxy
from Src.Logics.convert_factory import convert_factory
from Src.Logics.storage_observer import storage_observer

import os
import json
from datetime import datetime

#
# Сервис логирования
#
class console_log_service(service):

    __storage: storage = None
    __item:error_proxy = None

    def __init__(self, data: list = None) -> None:
        super().__init__(data)
        self.__storage = storage()
        self.__data = []
        storage_observer.append(self)

    @property
    def item(self) -> error_proxy:
        return self.__item

    @item.setter
    def item(self, value: error_proxy):
        exception_proxy.validate(value, error_proxy)
        self.__item = value

    def __observe_print_log(self):
        """
            Вывести лог в консоль
        """
        data = self.__data
        period =  datetime.now().strftime('%Y-%m-%d')
        factory = convert_factory()
        data = factory.serialize( data )
        json_text = json.dumps(data, sort_keys = True, indent = 4, ensure_ascii = False)
        print(f"{period}:  {json_text}")





    def handle_event(self, handle_type: str ):
        """
            Обработать событие
        Args:
            handle_type (str): Ключ
        """
        super().handle_event(handle_type)

        # Добавить запись в лог
        if handle_type == event_type.write_log() and self.__item is not None:
            self.__data.append(self.__item)

        # Вывести лог в консоль
        if handle_type == event_type.save_log():
            self.__observe_print_log()