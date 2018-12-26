import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from logistic import LogisticLattice
from progressbar import ProgressBar

"""
Coupled Map Lattice Evolution plotting functionality
- Takes any CML as input
- Handles visualization separately from CML simulation code
"""
class Evolution:

    def __init__(self, cml, colormap='plasma'):
        self.cml = cml

    def plot_time_evolution(self, iterations, modulus=1):

        # generate evolution data
        data = np.array(self.cml.get_lattice())
        bar = ProgressBar(max_value=(iterations-1))
        for i in range(iterations - 1):
            new_data = self.cml.update()
            if i % modulus == 0:
                data = np.vstack((data, new_data))
            bar.update(i)

        fig = plt.figure(figsize=(6, 3.2))
        ax = fig.add_subplot(111)
        ax.set_title('Lattice Evolution')
        plt.imshow(data)
        ax.set_aspect('equal')
        # we want the lattice "evolving upward"
        plt.gca().invert_yaxis()

        cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
        cax.get_xaxis().set_visible(False)
        cax.get_yaxis().set_visible(False)
        cax.patch.set_alpha(0)
        cax.set_frame_on(False)
        plt.colorbar(orientation='vertical')
        plt.show()


"""
lat = LogisticLattice(10, 0.5, 1.67)
ev = Evolution(lat)

ev.plot_time_evolution(4)
"""
