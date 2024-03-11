from Src.Logics.reporting import reporting
from Src.Logics.csv_reporting import csv_reporting
from Src.exceptions import exception_proxy, argument_exception
from Src.Logics.markdown_reporting import markdown_reporting

class report_factory:
    __maps = {}

    def __init__(self) -> None:
        self.__build_structure()
    
    def __build_structure(self):
        self.__maps["csv"] = csv_reporting
        self.__maps["md"] = markdown_reporting
        
