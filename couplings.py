import numpy as np

"""
Coupling schemes for CMLs
"""

class TwoNeighbor:
    def __init__(self, strength, map_obj):
        self.strength = strength
        self.map_obj = map_obj
        self.map_function = self.map_obj._map

    def boundary_update(self, end):
        return self.map_function(end)

    def neighbor_coupled_update(self, L, C, R):
        return (1.0 - self.strength) * self.map_function(C) + (self.strength/2.0) * (self.map_function(L) + self.map_function(R))

    def couple(self, lattice):
        lat = lattice
        # End values don't have two neighbors
        left_end = self.boundary_update(lat[0])
        right_end = self.boundary_update(lat[-1])
        # Simple two-neighbor coupling scheme
        """ BUG: test this on a simpler np array.
            It doesn't work / produce the desired functionality
        """
        # Doesn't this repeat the first value?
        middle_values = self.neighbor_coupled_update(lat[:-2], lat[1:-1], lat[2:])
        # Left end + middle + right end
        lat = np.insert(middle_values, 0, left_end, axis=0)
        lat = np.insert(lat, len(lat) - 1, right_end, axis=0)
        return lat
