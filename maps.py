"""
Map functions for CMLs
"""

class Map:
    def __init__(self, alpha):
        self.alpha = alpha
    def get_alpha(self):
        return self.alpha
    def set_alpha(self, alpha):
        self.alpha = alpha

class Logistic(Map):
    def __init__(self, alpha):
        Map.__init__(self, alpha)
    def _map(self, prev):
        return self.alpha * prev * (1.0 - prev)

class KanekoLogistic(Map):
    def __init__(self, alpha):
        Map.__init__(self, alpha)
    def _map(self, prev):
        return 1.0 - self.alpha * (prev ** 2)
