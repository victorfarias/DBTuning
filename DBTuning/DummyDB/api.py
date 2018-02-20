from collections import OrderedDict

import numpy as np


class DummyDB(object):

    def __init__(self):
        self.domain = [{
            'name': 'param1',
            'type': 'continuous',
            'domain': (0,1)
        },
        {
            'name': 'param2',
            'type': 'continuous',
            'domain': (0,1)
        },
        {
            'name': 'param3',
            'type': 'continuous',
            'domain': (0,1)
        },
        {
            'name': 'param4',
            'type': 'continuous',
            'domain': (0,1)
        }]
        self.params = OrderedDict(
            [(p['name'], 0.) for p in self.domain]
        )        


    def start(self):
        pass

    def stop(self):
        pass

    def set_param(self, name, value):
        self.params[name] = value

    def set_params(self, params):
        self.params = params

    def set_params_vector(self, v):
        for vs, k in zip(v, self.params.keys()):
            self.params[k] = vs

    def get_param(self, name):
        return self.params[name]

    def get_params(self):
        return self.params

    def params_vector(self):
        return np.array([v for v in self.params.values()])

    def collect_metric(self):
        return np.sin(np.sum(self.params_vector()))
