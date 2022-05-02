import numpy as np
import pandas as pd

from hr_collection.config import config
from hr_collection.hr_model.hr_classification import PromotionModel


def test_employees_promo():
    test_data = pd.read_csv(f"{config.DATASETS_DIR}/{config.PROMOTION_TEST_DATA_FILE_FR}")
    test_data = test_data.drop("Unnamed: 0", axis=1)
    len_test = len(test_data)

    promo_model = PromotionModel()
    subject = promo_model.make_prediction(test_data)

    assert subject is not None
    assert len(subject.get('predictions')) == len_test

def test_employee_promo():
    test_data = pd.read_csv(f"{config.DATASETS_DIR}/{config.PROMOTION_TEST_DATA_FILE_FR}")
    test_data = test_data.drop("Unnamed: 0", axis=1)
    single_test = test_data[0:1]

    promo_model = PromotionModel()
    subject = promo_model.make_prediction(single_test)

    assert subject is not None
    assert isinstance(subject.get('predictions')[0], np.int64)
