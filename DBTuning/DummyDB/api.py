
class DummyDB(object):

    def __init__(self):
        self.domain = [{
            'name': 'param',
            'type', 'continuous',
            'domain': (0,1)
        }]

    def start(self):
        pass

    def stop(self):
        pass

        