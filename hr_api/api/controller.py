from hr_api.api.validation import validate_inputs
from flask import Blueprint, request, jsonify
from hr_api.api.config import get_logger
from hr_collection.hr_model.hr_classification import AttritionModel, PromotionModel
from hr_collection import __version__ as api_version

from hr_api.api import __version__ as _version

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'

@prediction_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': _version,
                        'api_version': api_version})

@prediction_app.route('/v1/predict/attrition', methods=['POST'])
def predict__attrition():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        input_data, errors = validate_inputs(input_data=json_data, data_request='attrition')

        attrition = AttritionModel()
        result = attrition.make_prediction(input_data=input_data)
        _logger.info(f'Outputs: {result}')

        predictions = result.get('predictions').tolist()
        version = result.get('version')

        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})

@prediction_app.route('/v1/predict/promotion', methods=['POST'])
def predict__promotion():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        input_data, errors = validate_inputs(input_data=json_data, data_request='promotion')

        attrition = PromotionModel()
        result = attrition.make_prediction(input_data=input_data)
        _logger.info(f'Outputs: {result}')

        predictions = result.get('predictions').tolist()
        version = result.get('version')

        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})