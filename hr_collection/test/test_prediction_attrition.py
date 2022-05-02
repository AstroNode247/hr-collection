import pandas as pd
import numpy as np

from hr_collection import config
from hr_collection.hr_model.hr_classification import AttritionModel

def test_employees_attrition():
    test_data = pd.read_csv(f"{config.DATASETS_DIR}/{config.ATTRITION_TEST_DATA_FILE}")
    test_data = test_data.drop("Unnamed: 0", axis=1)
    len_test = len(test_data)

    attrition_model = AttritionModel()
    subject = attrition_model.make_prediction(test_data)

    assert subject is not None
    assert len(subject.get('predictions')) == len_test

def test_employee_attrition():
    test_data = pd.read_csv(f"{config.DATASETS_DIR}/{config.ATTRITION_TEST_DATA_FILE}")
    test_data = test_data.drop("Unnamed: 0", axis=1)
    single_data = test_data[0:1]

    attrition_model = AttritionModel()
    subject = attrition_model.make_prediction(single_data)

    assert subject is not None
    assert isinstance(subject.get('predictions')[0], np.int64)