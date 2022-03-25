import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class CustomTransformer(BaseEstimator):
    def __init__(self, variables=None):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables


class LogTransformer(CustomTransformer, TransformerMixin):
    def __init__(self, variables=None):
        super().__init__(variables)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = np.log10(X[feature].values)
        return X


class Imputer(CustomTransformer, TransformerMixin):
    def __init__(self, value=None, variables=None):
        super().__init__(variables)
        self.value = value

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].fillna(self.value)
        return X


class LabelTransformer(CustomTransformer, TransformerMixin):
    def __init__(self, variables=None):
        super().__init__(variables)

    def fit(self, X, y=None):
        return self

    def __label_travel(self, x):
        if x == "Voyage rarement":
            return 1
        if x == "Voyage frequemment":
            return 2
        if x == "Pas voyage":
            return 0
        return 0

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = X[feature].apply(self.__label_travel)
        return X


class TargetTransformer(CustomTransformer, TransformerMixin):
    def __init__(self, variables=None):
        super().__init__(variables)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        for feature in self.variables:
            X[feature] = [1 if a == "Oui" else 0 for a in X[feature]]
        return X


class SelectBestFeature(CustomTransformer, TransformerMixin):
    def __init__(self, variables=None):
        super().__init__(variables)

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X = X[self.variables]
        return X
