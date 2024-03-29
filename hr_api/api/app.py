from flask import Flask
from hr_api.api.config import get_logger

_logger = get_logger(logger_name=__name__)

def create_app(*, config_object) -> Flask:
    flask_app = Flask("hr_api")
    flask_app.config.from_object(config_object)

    from hr_api.api.controller import prediction_app
    flask_app.register_blueprint(prediction_app)
    _logger.debug('Application instance created')

    return flask_app