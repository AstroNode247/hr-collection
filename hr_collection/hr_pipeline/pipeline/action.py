from hr_collection.hr_pipeline.pipeline.base_pipeline import BaseData, LoadCSV, LoadDB


class Pipeline:
    def __init__(self, data):
        self.data = data

    def run(self):
        self.data.transform()

    def load_to_csv(self, output):
        loader = LoadCSV()
        loader.load(self.data.data, output)

    def load_to_db(self, output):
        loader = LoadDB()
        loader.load("promotion", self.data.data, output)
