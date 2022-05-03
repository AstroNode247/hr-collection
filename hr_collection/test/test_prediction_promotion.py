import numpy as np
import pandas as pd
from sklearn.datasets import load_diabetes

from hr_collection.config import config
from hr_collection.hr_model.hr_classification import PromotionModel


def test_employees_promo():
    promo_model = PromotionModel()
    test_data = promo_model.load_dataset()
    len_test = len(test_data)

    subject = promo_model.make_prediction(test_data)

    assert subject is not None
    assert len(subject.get('predictions')) == len_test

def test_employee_promo():
    promo_model = PromotionModel()
    test_data = promo_model.load_dataset()
    single_test = test_data[0:1]

    subject = promo_model.make_prediction(single_test)

    assert subject is not None
    assert isinstance(subject.get('predictions')[0], np.float64)
