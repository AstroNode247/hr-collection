from flask import Blueprint, request, jsonify
from api.config import get_logger
from hr_collection.hr_model.hr_classification import AttritionModel, PromotionModel

_logger = get_logger(logger_name=__name__)

prediction_app = Blueprint('prediction_app', __name__)

@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'

@prediction_app.route('/v1/predict/attrition', methods=['POST'])
def predict__attrition():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        attrition = AttritionModel()
        result = attrition.make_prediction(input_data=json_data)
        _logger.info(f'Outputs: {result}')

        predictions = int(result.get('predictions')[0])
        version = result.get('version')

        return jsonify({'predictions': predictions,
                        'version': version})

@prediction_app.route('/v1/predict/promotion', methods=['POST'])
def predict__promotion():
    if request.method == 'POST':
        json_data = request.get_json()
        _logger.info(f'Inputs: {json_data}')

        attrition = PromotionModel()
        result = attrition.make_prediction(input_data=json_data)
        _logger.info(f'Outputs: {result}')

        predictions = int(result.get('predictions')[0])
        version = result.get('version')

        return jsonify({'predictions': predictions,
                        'version': version})