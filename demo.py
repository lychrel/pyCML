from cml import CML
from maps import KanekoLogistic
from couplings import TwoNeighbor
from evolution import Evolution

cml = CML(dim=100,
          coupling=TwoNeighbor(strength=0.2,
                               map_obj=KanekoLogistic(alpha=1.47)))

ev = Evolution(cml)
ev.plot_time_evolution(10)
