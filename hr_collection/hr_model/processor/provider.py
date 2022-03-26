from abc import ABC, abstractmethod

import joblib


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
        save_file_name = f"{name}.pkl"
        save_path = model_dir / save_file_name
        self._remove_old_pipelines(files_to_keep=[save_file_name], model_dir=model_dir)
        print("Save the model to a pickle")
        joblib.dump(pipeline, save_path)
