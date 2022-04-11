import pandas as pd

from hr_collection.config import config
from hr_collection.hr_model.hr_classification import PromotionModel


def test_employee_promo():
    test_data = pd.read_csv(f"{config.DATASETS_DIR}/{config.PROMOTION_TEST_DATA_FILE_FR}")
    test_data = test_data.drop("Unnamed: 0", axis=1)

    promo_model = PromotionModel()
    subject = promo_model.make_prediction(test_data)

    assert subject is not None
