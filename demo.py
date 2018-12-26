from logistic import LogisticLattice
import numpy as np
from array2gif import write_gif
import matplotlib.pyplot as plt
from progressbar import ProgressBar

from cml import CML
from maps import KanekoLogistic
from couplings import TwoNeighbor
from evolution import Evolution

"""
BUG: doesn't work
"""

cml = CML(dim=100, coupling=TwoNeighbor(strength=0.2, map_obj=KanekoLogistic(alpha=1.47)))

ev = Evolution(cml)
ev.plot_time_evolution(10)
