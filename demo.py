from cml import CML
from maps import KanekoLogistic
from couplings import TwoNeighbor
from evolution import Evolution

cml = CML(dim=100,
          coupling=TwoNeighbor(strength=0.5,
                               map_obj=KanekoLogistic(alpha=1.47)))

ev = Evolution(cml)
#ev.time_evolution(12000, 12, True, True, True)
ev.alpha_evolution()
