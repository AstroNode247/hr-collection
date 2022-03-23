import pathlib
import hr_collection
from urllib.parse import quote

PACKAGE_ROOT = pathlib.Path(hr_collection.__file__).resolve().parent
DATASETS_DIR = PACKAGE_ROOT / "datasets"

PROMOTION_DATA_FILE = "employee_promo_train.csv"
ATTRITION_DATA_FILE = "general_data.csv"

POSTGRES_CONN = "postgresql://postgres:%s@localhost:5432/hr_collection" % quote("adm!@#")
