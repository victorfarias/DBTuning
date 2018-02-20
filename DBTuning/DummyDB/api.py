
class DummyDB(object):

    def __init__(self):
        self.domain = [{
            'name': 'param1',
            'type', 'continuous',
            'domain': (0,1)
        }]
        self.params = {
            param1 : 0.5
        }

    def start(self):
        pass

    def stop(self):
        pass

    def set_param(self, name, value):
        self.params[name] = value

    def set_params(self, params):
        self.params = params

    def collect_metric(self):
        return self.params['param1']**2