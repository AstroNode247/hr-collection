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
    def load(self, data, output):
        pass


class LoadCSV(Loader):
    def load(self, data, output):
        data.to_csv(output)


class LoadDB(Loader):
    def load(self, table, data, conn):
        engine = create_engine(conn)
        data.to_sql(table, con=engine, if_exists="replace", index=False)
