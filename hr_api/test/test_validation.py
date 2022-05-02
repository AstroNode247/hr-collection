import json
import pandas as pd

from hr_collection.config import config

def test_prediction_endpoint_attrition_validation_200(flask_test_client):
    test_data = pd.read_csv(f"{config.DATASETS_DIR}/{config.ATTRITION_TEST_DATA_FILE}")
    test_data = test_data.drop("Unnamed: 0", axis=1)
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
    test_data = pd.read_csv(f"{config.DATASETS_DIR}/{config.PROMOTION_TEST_DATA_FILE_FR}")
    test_data = test_data.drop("Unnamed: 0", axis=1)
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