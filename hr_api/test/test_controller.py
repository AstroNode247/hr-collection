import pandas as pd
import json
import math

from hr_collection.config import config
from hr_collection.hr_model.hr_classification import AttritionModel, PromotionModel
from hr_collection import __version__ as api_version

from hr_api.api import __version__ as _version

def test_health_endpoint_returns_200(flask_test_client):
    # When
    response = flask_test_client.get('/health')

    # Then
    assert response.status_code == 200

def test_version_endpoint_returns_version(flask_test_client):
    # When
    response = flask_test_client.get('/version')

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    assert response_json['model_version'] == _version
    assert response_json['api_version'] == api_version


def test_prediction_endpoint_returns_attrition_prediction(flask_test_client):
    # Given
    test_data = AttritionModel().load_dataset()
    post_json = test_data[0:1].to_json(orient='records')
    post_json = json.loads(post_json)

    # When
    response = flask_test_client.post('/v1/predict/attrition',
                                      json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    response_version = response_json['version']
    assert response_version == api_version

def test_prediction_endpoint_returns_promotion_prediction(flask_test_client):
    # Given
    test_data = PromotionModel().load_dataset()
    post_json = test_data[0:1].to_json(orient='records')
    post_json = json.loads(post_json)

    # When
    response = flask_test_client.post('/v1/predict/promotion',
                                      json=post_json)

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)
    prediction = response_json['predictions']
    response_version = response_json['version']
    assert response_version == api_version
