from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

from hr_collection.hr_model.processor import preprocessor as pp

from hr_collection.config import config, features
import pandas as pd

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from hr_collection.hr_model.base_model import BaseModel, EvaluationMixin, PickleMixin


class AttritionModel(BaseModel, EvaluationMixin, PickleMixin):
    def __init__(self):
        super().__init__()
        self._algorithm = RandomForestClassifier()
        self._features = {'features': features.ATTRITION_FEATURES,
                          'target': features.ATTRITION_TARGET}
        self.model_dir = {'directory': config.ATTRITION_MODEL_DIR,
                          'file': config.ATTRITION_MODEL_NAME}

    def _load_dataset(self):
        self._data = pd.read_csv(f"{config.DATASETS_DIR}/{config.ATTRITION_DATA_FILE_FR}")
        self._data = self._data.drop("Unnamed: 0", axis=1)

        numerical_transformer = Pipeline([
            ("numerical_imputer", pp.Imputer(value=0, variables=features.ATTRITION_NUM_FEATURES)),
            ("log_transformer", pp.LogTransformer(variables=features.ATTRITION_SKEWED_FEATURES))
        ])

        preprocessor = ColumnTransformer([
            ("numerical_transformer", numerical_transformer, features.ATTRITION_NUM_FEATURES),
            ("label_transformer", pp.LabelTransformer(variables=features.ATTRITION_LABELED_FEATURES),
             features.ATTRITION_LABELED_FEATURES),
            ("categorical_transformer", OneHotEncoder(handle_unknown='ignore', sparse=False),
             features.ATTRITION_CAT_FEATURES)
        ])

        self.pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("model", self._algorithm)
        ])

        return self._data

    def train(self, test_size, random_state):
        self._data = self._load_dataset()

        target_encoder = pp.TargetTransformer(variables=features.ATTRITION_TARGET)
        self._data = target_encoder.transform(self._data)

        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(
            self._data[self._features['features']], self._data[self._features['target']],
            test_size=test_size, random_state=random_state
        )

        print("Train the model....")
        self.pipeline.fit(self._X_train, self._y_train)
        print("Training finished with success....")


class PromotionModel(BaseModel, EvaluationMixin, PickleMixin):
    def __init__(self):
        super().__init__()
        self._algorithm = AdaBoostClassifier(n_estimators=100)

        self._features = {'features': features.PROMOTION_FEATURES,
                          'target': features.PROMOTION_TARGET}
        self.model_dir = {'directory': config.PROMOTION_MODEL_DIR,
                          'file': config.PROMOTION_MODEL_NAME}

    def _load_dataset(self):
        self._data = pd.read_csv(f"{config.DATASETS_DIR}/{config.PROMOTION_DATA_FILE_FR}")
        self._data.drop('Unnamed: 0', axis=1)

        categorical_transformer = Pipeline([
            ("fill_na_nivDiplome", pp.Imputer('Missing', features.PROMOTION_CAT_MISSING)),
            ("categorical_encoding", OneHotEncoder(categories='auto'))
        ])
        numerical_transformer = Pipeline([
            ("numeriacal_transformer", pp.Imputer(3, features.PROMOTION_NUM_MISSING)),
            ("minmax_scaler", MinMaxScaler())
        ])

        preprocessor = ColumnTransformer([
            ("categorical_transformer", categorical_transformer, features.PROMOTION_CAT_FEATURES),
            ("numerical_transformer", numerical_transformer, features.PROMOTION_NUM_FEATURES)
        ])

        self.pipeline = Pipeline([
            ("preprocessor", preprocessor),
            ("ada_boost", self._algorithm)
        ])

        return self._data
