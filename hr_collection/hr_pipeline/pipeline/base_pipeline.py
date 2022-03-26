from abc import ABC, abstractmethod

import pandas as pd
from sqlalchemy import create_engine


class BaseData(ABC):
    def __init__(self):
        self.data = None


class ITransformer:
    @abstractmethod
    def transform(self):
        pass


class Loader:
    @abstractmethod
    def load(self, data, output, conn=None):
        pass


class LoadCSV(Loader):
    def load(self, data, output, conn=None):
        print("Save the data to csv file...")
        data.to_csv(output)
        print("CSV file has been saved successfully")


class LoadDB(Loader):
    def load(self, data, output, conn=None):
        engine = create_engine(conn)
        print("Load the data to DB...")
        data.to_sql(output, con=engine, if_exists="replace", index=False)
        print("Load is done successfully")
