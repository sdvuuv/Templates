from Src.Logics.Services.service import service
from Src.exceptions import exception_proxy, operation_exception
from Src.reference import reference
from Src.Logics.storage_observer import storage_observer
from Src.Models.event_type import event_type
from Src.Logics.Services.post_processing_service import post_processing_service
from Src.Logics.logging_observer import logging_observer
from Src.Models.log_model import log_model
from Src.settings_manager import settings_manager


#
# Сервис для выполнения CRUD операций
#
class reference_service(service):
    options = settings_manager()

    def __init__(self, data: list) -> None:
        super().__init__(data)
        storage_observer.observers.append(self)
        post_processing_service(self.data)

    def add(self, item: reference) -> bool:
        """
            Добавить новый элемент
        """
        exception_proxy.validate(item, reference)
        found = list(filter(lambda x: x.id == item.id, self.data))
        if len(found) > 0:
            return False

        self.data.append(item)
        log = log_model()
        log.name = "add log"
        log.construct_log(self.options.settings.logging_categories["reference_service"], "reference_service_add()",
                          "Success")
        logging_observer.observers.append(log)
        return True

    def delete(self, item: reference) -> bool:
        """
            Удалить элемент
        """
        exception_proxy.validate(item, reference)
        found = list(filter(lambda x: x.id == item.id, self.data))
        if len(found) == 0:
            return False
        item = found[0]

        # Найти нужный наблюдатель и вызвать событие
        observer_item = storage_observer.get(storage_observer.post_processing_service_key())
        observer_item.nomenclature = item
        storage_observer.raise_event(event_type.deleted_nomenclature())

        # Удалить элемент
        self.data.remove(item)

        log = log_model()
        log.name = "delete log"
        log.construct_log(self.options.settings.logging_categories["reference_service"], "reference_service_delete()",
                          "Success")
        logging_observer.observers.append(log)

        return True

    def change(self, item: reference) -> bool:
        """
            Изменить элемент
        """
        exception_proxy.validate(item, reference)
        found = list(filter(lambda x: x.id == item.id, self.data))
        if len(found) == 0:
            return False

        self.delete(found[0])
        self.add(item)

        log = log_model()
        log.name = "change log"
        log.construct_log(self.options.settings.logging_categories["reference_service"], "reference_service_change()",
                          "Success")
        logging_observer.observers.append(log)

        return True

    def get(self) -> list:
        """
            Вернуть список
        """

        log = log_model()
        log.name = "get log"
        log.construct_log(self.options.settings.logging_categories["reference_service"], "reference_service_get()",
                          "Success")
        logging_observer.observers.append(log)

        return self.data

    def get_item(self, id: str) -> reference:
        """
            Вернуть элемент
        """
        exception_proxy.validate(id, str)
        found = list(filter(lambda x: x.id == id, self.data))
        if len(found) == 0:
            raise operation_exception(f"Не найден элемент с кодом {id}!")

        log = log_model()
        log.name = "delete log"
        log.construct_log(self.options.settings.logging_categories["reference_service"], "reference_service_get_item()",
                          "Success")
        logging_observer.observers.append(log)

        return found

    def handle_event(self, handle_type: str):
        """
            Обработать событие
        Args:
            handle_type (str): _description_
        """
        super().handle_event(handle_type)





