import pandas as pd
import numpy as np

from hr_collection import config
from hr_collection.hr_model.hr_classification import AttritionModel

def test_employees_attrition():
    attrition_model = AttritionModel()
    test_data = attrition_model.load_dataset()
    len_test = len(test_data)

    subject = attrition_model.make_prediction(test_data)

    assert subject is not None
    assert len(subject.get('predictions')) == len_test

def test_employee_attrition():
    attrition_model = AttritionModel()
    test_data = attrition_model.load_dataset()
    single_data = test_data[0:1]

    subject = attrition_model.make_prediction(single_data)

    assert subject is not None
    assert isinstance(subject.get('predictions')[0], np.int64)