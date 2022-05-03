import json
import pandas as pd

from hr_collection.config import config
from hr_collection.hr_model.hr_classification import AttritionModel, PromotionModel

def test_prediction_endpoint_attrition_validation_200(flask_test_client):
    test_data = AttritionModel().load_dataset()
    post_json = test_data.to_json(orient='records')
    post_json = json.loads(post_json)

    # When
    response = flask_test_client.post('/v1/predict/attrition',
                                      json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)

    # Check correct number of errors removed
    assert len(response_json.get('predictions')) + len(
        response_json.get('errors')) == len(test_data)

def test_prediction_endpoint_promotion_validation_200(flask_test_client):
    test_data = PromotionModel().load_dataset()
    post_json = test_data.to_json(orient='records')
    post_json = json.loads(post_json)

    # When
    response = flask_test_client.post('/v1/predict/promotion',
                                      json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)

    # Check correct number of errors removed
    assert len(response_json.get('predictions')) + len(
        response_json.get('errors')) == len(test_data)