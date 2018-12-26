import numpy as np

"""
Coupled Map Lattice with
- Two-Neighbor coupling of strength 'coupling'
- Local logistic maps with parameter 'alpha'
- Number of lattice points 'dim'
"""
class CML:

    def __init__(self, dim, coupling):
        self.lattice = np.random.uniform(0, 1, (dim))
        self.dim = dim
        self.coupling = coupling

    def update(self):
        self.lattice = self.coupling.couple(self.lattice)
        return self.lattice

    # retrieve lattice values
    def get_lattice(self):
        return self.lattice

"""
lat = LogisticLattice(10, 0.4, 1.71)
for i in range(20):
    print(lat.update())
    print("\n")
"""
