from Src.Models.storage_transaction_model import storage_transaction_model
from Src.Models.storage_turn_model import storage_turn_model
from Src.Models.storage_model import storage_model
from Src.Models.storage_type_model import storage_type_model


class process_factory:

    def process_storage_turn(transactions_list: list) -> list:
        # Словарь, ключ - кортеж из номенклатуры, единицы измерения, склада и типа операции
        turn_dict = {}

        result = []
        # Перебор всех транзакций в списке и передача данных в словарь
        for transaction in transactions_list:
            if (transaction.nomenclature, transaction.unit, transaction.storage, transaction.operation_type) not in turn_dict.keys():
                turn_dict[(transaction.nomenclature,
                           transaction.unit, transaction.storage)] = 0
            if transaction.operation_type.name == "Addition":
                turn_dict[(transaction.nomenclature, transaction.unit,
                           transaction.storage)] += transaction.quantity
            elif transaction.operation_type.name == "Substraction":
                turn_dict[(transaction.nomenclature, transaction.unit,
                           transaction.storage)] -= transaction.quantity

        for key_list in turn_dict.keys():
            turn = storage_turn_model("0")
            turn.nomenclature = key_list[0]
            turn.unit = key_list[1]
            turn.storage = key_list[2]
            turn.quantity = turn_dict[key_list]
            result.append(turn)

        return result
