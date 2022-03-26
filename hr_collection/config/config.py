import pathlib
import hr_collection
from urllib.parse import quote

PACKAGE_ROOT = pathlib.Path(hr_collection.__file__).resolve().parent
DATASETS_DIR = PACKAGE_ROOT / "datasets"

PROMOTION_DATA_FILE = "employee_promo_train.csv"
PROMOTION_DATA_FILE_FR = "employee_promo_fr.csv"

PROMOTION_TEST_DATA_FILE_FR = "employee_promo_test_fr.csv"
PROMOTION_TEST_DATA_FILE = "employee_promo_test.csv"


ATTRITION_DATA_FILE = "general_data.csv"
ATTRITION_DATA_FILE_FR = "generaL_data_fr.csv"

POSTGRES_CONN = "postgresql://postgres:%s@localhost:5432/hr_collection" % quote("adm!@#")

TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_model"

ATTRITION_MODEL_DIR = TRAINED_MODEL_DIR / "attrition_trained_model"
ATTRITION_MODEL_NAME = "attrition_classifier"
PROMOTION_MODEL_DIR = TRAINED_MODEL_DIR / "promotion_trained_model"
PROMOTION_MODEL_NAME = "promotion_classifier"

