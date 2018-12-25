from logistic import LogisticLattice
import numpy as np
from array2gif import write_gif
import matplotlib.pyplot as plt
from progressbar import ProgressBar

"""
BUG: doesn't work
"""

lat = LogisticLattice(10, 0.3, 1.75)

dataset = []
bar = ProgressBar(max_value=100)
for i in range(100):
    up = lat.update()
    up = up.reshape(1, 10, 10)
    up = np.uint8(255 * up)
    dataset.append(np.concatenate((up, up, up), axis=0))
    bar.update(i)

write_gif(dataset, 'tmp.gif', fps=5)
