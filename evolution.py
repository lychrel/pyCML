import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from progressbar import ProgressBar
from array2gif import write_gif

"""
Coupled Map Lattice Evolution plotting functionality
- Takes any CML as input
- Handles visualization separately from CML simulation code
"""
class Evolution:

    def __init__(self, cml, colormap='plasma'):
        self.cml = cml
        self.colormap = colormap

    def time_evolution(self, iterations, modulus=1, save_figure=False, save_data=False, show_figure=True):

        # generate evolution data
        data = np.array(self.cml.get_lattice())
        bar = ProgressBar(max_value=(iterations-1))
        for i in range(iterations - 1):
            new_data = self.cml.update()
            if i % modulus == 0:
                data = np.vstack((data, new_data))
            bar.update(i)

        """
        for nice blurring
        from scipy.ndimage.filters import gaussian_filter
        data = gaussian_filter(data, sigma=7)
        """

        if save_data:
            np.save("time_evolution.npy", data)

        fig = plt.figure(figsize=(6, 3.2))
        ax = fig.add_subplot(111)
        ax.set_title('Lattice Evolution')
        plt.imshow(data, cmap=self.colormap)
        ax.set_aspect('equal')
        # we want the lattice "evolving upward"
        plt.gca().invert_yaxis()

        cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
        cax.get_xaxis().set_visible(False)
        cax.get_yaxis().set_visible(False)
        cax.patch.set_alpha(0)
        cax.set_frame_on(False)
        plt.colorbar(orientation='vertical')

        if save_figure:
            plt.savefig("time_evolution.png")

        if show_figure:
            plt.show()

        return data

    def alpha_evolution(self, steps=100, time_iterations=100, max=2.0, min=1.5, save_figure=True, save_data=False):

        # First, generate all data
        data_array = []
        rgb_data_array = []
        for index, al in enumerate(np.linspace(min, max, steps)):
            print("Evolution {} out of {}...".format(index, steps))
            # Update CML's alpha value
            self.cml.coupling.map_obj.set_alpha(al)
            data = self.time_evolution(time_iterations, 1, False, False, False)

            # For now: artificial RGB for array2gif
            g_to_rgb = lambda x: [x, x, x]

            rgb_data = []
            for row in data:
                rgb_row = []
                for val in row:
                    rgb_row.append(g_to_rgb(val))
                rgb_data.append(rgb_row)

            rgb_data = np.array(rgb_data)

            rgb_data = (rgb_data + 1.0) * 255.0 / 2.0
            rgb_data = rgb_data.astype(int)

            data_array.append(data)
            rgb_data_array.append(rgb_data)

        if save_figure:
            write_gif(rgb_data_array, "alpha_evolution.gif", fps=10)

        if save_data:
            np.save("alpha_evolution.npy", np.array(data_array))





"""
cml = CML(dim=100, coupling=TwoNeighbor(strength=0.2, map_obj=KanekoLogistic(alpha=1.47)))

ev = Evolution(cml)
ev.plot_time_evolution(10)
"""
