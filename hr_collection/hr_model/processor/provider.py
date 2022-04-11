from abc import ABC, abstractmethod

import joblib
from hr_collection import __version__ as _version

import logging
_logger = logging.getLogger(__name__)


class ModelProvider(ABC):
    @abstractmethod
    def load(self, file, model_dir):
        pass

    @abstractmethod
    def save(self, name, model_dir, pipeline):
        pass

    def _remove_old_pipelines(self, files_to_keep, model_dir):
        do_not_delete = files_to_keep + ['__init__.py']
        for model_file in model_dir.iterdir():
            if model_file.name not in do_not_delete:
                model_file.unlink()


class PickleProvider(ModelProvider):
    __instance = None

    @staticmethod
    def get_model_provider():
        if PickleProvider.__instance is None:
            PickleProvider.__instance = PickleProvider()
        return PickleProvider.__instance

    def load(self, file, model_dir):
        path = model_dir / file
        trained_model = joblib.load(filename=path)
        return trained_model

    def save(self, name, model_dir, pipeline):
        save_file_name = f"{name}{_version}.pkl"
        save_path = model_dir / save_file_name
        self._remove_old_pipelines(files_to_keep=[save_file_name], model_dir=model_dir)
        joblib.dump(pipeline, save_path)
        _logger.info(f"save pipeline : {save_file_name}")
