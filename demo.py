from cml import CML
from maps import KanekoLogistic
from couplings import TwoNeighbor
from evolution import Evolution

cml = CML(dim=1000,
          coupling=TwoNeighbor(strength=0.00115,
                               map_obj=KanekoLogistic(alpha=1.7522)))

ev = Evolution(cml)
ev.time_evolution(12000, 12, True, True, True)
