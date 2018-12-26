"""
Map functions for CMLs
"""

class Logistic:
    def __init__(self, alpha):
        self.alpha = alpha
    def _map(self, prev):
        return self.alpha * prev * (1.0 - prev)

class KanekoLogistic:
    def __init__(self, alpha):
        self.alpha = alpha
    def _map(self, prev):
        return 1.0 - self.alpha * (prev ** 2)
