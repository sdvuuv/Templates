from Src.exceptions import argument_exception
from Src.Logics.Services.service import service
from Src.Logics.storage_observer import storage_observer
from Src.Models.event_type import event_type
from Src.Storage.storage import storage
import uuid



class post_processing_service(service):
    __nomenclature_id = None
    __storage = None

    def __init__(self, data: list):
        super().__init__(data)
        self.__storage = storage()
        storage_observer.observers.append(self)

    @property
    def nomenclature_id(self):
        return self.__nomenclature_id

    @nomenclature_id.setter
    def nomenclature_id(self, nom_id: uuid.UUID):
        if not isinstance(nom_id, uuid.UUID):
            raise argument_exception("неверный тип аргумента")
        storage_observer.observers.append(self)
        self.__nomenclature_id = nom_id

    def handle_event(self, handle_type: str):
        super().handle_event(handle_type)

        if handle_type == event_type.deleted_nomenclature():
            self.clear_reciepe()


    def clear_reciepe(self):
        key = storage.receipt_key()
        for index, cur_rec in enumerate(self.__storage.data[key]):
            for cur_row in list(cur_rec.consist.values()):
                if self.__nomenclature_id == cur_row.nomenclature.id:
                    cur_rec.delete(cur_row)