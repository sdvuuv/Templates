from Src.exceptions import exception_proxy
from Src.exceptions import exception_proxy, argument_exception
#
# Класс для описания настроек
#
class settings():
    _short_name = ''
    _inn = 0
    _account = 0
    _corr_account = 0
    _BIK = 0
    _type = ""
    is_first_start = True
    _rep_format = ''


    @property
    def inn(self):
        return self._inn
    @inn.setter
    def inn(self, value: int):
        exception_proxy.validate(value, int)
        if len(str(value)) == 12:
            self._inn = value
        else:
            raise argument_exception("Передаваемая длина ИНН не соответстует заднным ограничениям")

    @property
    def short_name(self):
        return self._short_name

    @short_name.setter
    def short_name(self, value: str):
        exception_proxy.validate(value, str)
        self._short_name = value

    @property
    def account(self):
        return self._account

    @account.setter
    def account(self, value: int):
        '''
        Счёт
        '''
        if len(str(value)) == 11:
            self._account = value
        else:
            raise argument_exception("Передаваемая длина счета не соответстует заднным ограничениям")

    @property
    def correspondent_account(self):
        return self._corr_account

    @correspondent_account.setter
    def correspondent_account(self, value: int):
        '''
        Корреспонденский счёт
        '''
        if len(str(value)) == 11:
            self._corr_account = value
        else:
            raise argument_exception("Передаваемая длина корреспонденского счета не соответстует заднным ограничениям")

    @property
    def BIK(self):
        return self._BIK

    @BIK.setter
    def BIK(self, value: int):
        '''
        БИК
        '''
        if len(str(value)) == 9:
            self._BIK = value
        else:
            raise argument_exception("Передаваемая длина БИК не соответстует заднным ограничениям")

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value: str):
        '''
        Вид собственности
        '''
        if len(value) < 5:
            self._type = value
        else:
            raise argument_exception("Некорректный вид собственности")
    @property
    def is_first_start(self):
        """
           Флаг Первый старт
        """
        return self.is_first_start
            
    @is_first_start.setter        
    def is_first_start(self, value: bool):
        self._first_start = value

    @property
    def report_format(self):
        return self.__rep_format


    @report_format.setter
    def report_format(self, value: str):
        self.__rep_format = value