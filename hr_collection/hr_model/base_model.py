from abc import ABC, abstractmethod
from collections import defaultdict

import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score
from sklearn.model_selection import train_test_split

from hr_collection.hr_model import hr_classification
from hr_collection.hr_model.processor.provider import PickleProvider
from hr_collection.hr_model.processor.validation import validate_input_promotion, validate_input_attrition
from hr_collection import __version__ as _version

import logging
_logger = logging.getLogger(__name__)


class BaseModel(ABC):
    def __init__(self):
        self._algorithm = None
        self._data = None
        self.pipeline = None
        self._features = defaultdict()
        self._X_train, self._X_test, self._y_train, self._y_test = 0, 0, 0, 0
        self.model_dir = None

    @abstractmethod
    def load_dataset(self):
        pass

    @abstractmethod
    def _get_data(self):
        pass

    def train(self, test_size, random_state):
        self._data = self._get_data()
        self._X_train, self._X_test, self._y_train, self._y_test = train_test_split(
            self._data[self._features['features']], self._data[self._features['target']],
            test_size=test_size, random_state=random_state
        )

        print("Train the model...")
        self.pipeline.fit(self._X_train, self._y_train)
        print("Train is finish with sucess...\n")

    def predict(self):
        return self.pipeline.predict(self._X_test), self.pipeline.predict(self._X_train)

    def make_prediction(self, input_data):
        data = pd.DataFrame(input_data)
        if isinstance(self, hr_classification.PromotionModel):
            data = validate_input_promotion(data)
        if isinstance(self, hr_classification.AttritionModel):
            data = validate_input_attrition(data)
            
        pickleModel = PickleProvider.get_model_provider()
        model_pipeline = pickleModel.load(f"{self.model_dir['file']}{_version}.pkl", self.model_dir['directory'])

        prediction = model_pipeline.predict(data)
        results = {'predictions': prediction, 'version': _version}

        _logger.info(
            f"Making prediction with model version : {_version} "
            f"Inputs : {data}"
            f" Predictions : {results}"
        )

        return results


class EvaluationMixin:
    def evaluate(self):
        y_test_pred, y_train_pred = self.predict()
        print("Accuracy score : ", accuracy_score(self._y_test, y_test_pred))
        print("Recall score : ", recall_score(self._y_test, y_test_pred))
        print("Precision score : ", precision_score(self._y_test, y_test_pred))
        print("F1 score : ", f1_score(self._y_test, y_test_pred))

        print("\nAccuracy score on training set : ", accuracy_score(self._y_train, y_train_pred))
        print("Recall score training set : ", recall_score(self._y_train, y_train_pred))
        print("Precision score training set : ", precision_score(self._y_train, y_train_pred))
        print("F1 score training set : ", f1_score(self._y_train, y_train_pred))


class PickleMixin:
    pickleProvider = PickleProvider.get_model_provider()

    def save_pickle(self, name):
        _logger.info(f"saving model version : {_version}")
        self.pickleProvider.save(name, self.model_dir['directory'], self.pipeline)

    def load_pickle(self, name):
        print("Load the pipeline")
        return self.pickleProvider.load(name, self.model_dir)
