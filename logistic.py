import numpy as np

"""
Coupled Map Lattice with
- Two-Neighbor coupling of strength 'coupling'
- Local logistic maps with parameter 'alpha'
- Number of lattice points 'dim'
"""
class LogisticLattice:

    def __init__(self, dim, coupling=0.2, alpha=0.2):
        self.lattice = np.random.uniform(0, 1, (dim))
        self.coupling = coupling
        self.dim = dim
        self.alpha = alpha

    # logistic map
    def logistic(self, prev):
        return self.alpha * prev * (1.0 - prev)

    # general "next state" function
    def next_state(self, prev):
        #vec_logistic = np.vectorize(self.logistic)
        #return vec_logistic(prev)
        return self.logistic(prev)

    # update a lattice boundary
    def boundary_update(self, end):
        return self.logistic(end)

    # two-neighbor coupling
    def neighbor_coupled_update(self, L, C, R):
        return (1.0 - self.coupling) * self.next_state(C) + (self.coupling/2.0) * (self.next_state(L) + self.next_state(R))

    # update lattice values
    def update(self):
        lat = self.lattice
        # End values don't have two neighbors
        left_end = self.boundary_update(lat[0])
        right_end = self.boundary_update(lat[-1])
        # Simple two-neighbor coupling scheme
        """ BUG: test this on a simpler np array.
            It doesn't work / produce the desired functionality
        """
        middle_values = self.neighbor_coupled_update(lat[:-2], lat[1:-1], lat[2:])
        # Left end + middle + right end
        lat = np.insert(middle_values, 0, left_end, axis=0)
        lat = np.insert(lat, len(lat) - 1, right_end, axis=0)
        self.lattice = lat
        return lat

    # retrieve lattice values
    def get_lattice(self):
        return self.lattice

"""
lat = LogisticLattice(10, 0.4, 1.71)
for i in range(20):
    print(lat.update())
    print("\n")
"""
