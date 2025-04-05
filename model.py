# h2o_ml_wrapper/model.py

import h2o
from h2o.estimators import H2OGradientBoostingEstimator
from h2o.frame import H2OFrame

class H2OModel:
    def __init__(self):
        h2o.init()
        self.model = H2OGradientBoostingEstimator()

    def train(self, data_path, target):
        data = h2o.import_file(data_path)
        features = [col for col in data.col_names if col != target]
        self.model.train(x=features, y=target, training_frame=data)

    def predict(self, data_path):
        data = h2o.import_file(data_path)
        return self.model.predict(data).as_data_frame()

