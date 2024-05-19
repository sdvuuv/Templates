from Src.reference import reference
from datetime import datetime
from Src.Models.event_type import event_type
from Src.Storage.storage import storage


class log_model(reference):
    __log_info = ""

    def __init__(self):
        super().__init__()

    @property
    def log_info(self) -> str:
        return self.__log_info

    def construct_log(self, type: str, origin: str, status: str):
        self.__log_info = f"Log Type: {type}\nLog origin: {origin}\nOperation status: {status}\nDatetime of execution: {datetime.now()}"

    def handle_event(self, handle_type: str):
        """
            Обработать событие
        Args:
            handle_type (str): _description_
        """
        if handle_type == event_type.loggable_operation():
            key = storage.logs_key()
            data = storage().data[key]
            data.append(self)