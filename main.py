from flask import Flask
from Src.Logics.start_factory import start_factory
from Src.settings_manager import settings_manager
from Src.Logics.report_factory import report_factory
from Src.exceptions import error_proxy
app = Flask(__name__)

@app.route("/api/report/<storage_key>", methods = ["GET"])
def get_report(storage_key: str):
    """
        Отправить отчет на сервер
    """
    manager = settings_manager()
    start = start_factory(manager.settings)
    start.create()
    factory = report_factory()
    if storage_key in start.storage.data.keys():
        result = factory.create(manager.settings.report_mode, start.storage.data).create(storage_key)
    else:
        raise error_proxy('Неверный ключ!')
    
    response_type = app.response_class(
        response = f" key: {storage_key}\n result: {result}",
        status = 200,
        mimetype = "application/text"
    )

    return response_type


if __name__ == "__main__":
    app.run(debug = True)