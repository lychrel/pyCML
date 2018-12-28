# pyCML
For rapid construction and simulation of CMLs
---
## Getting Started
1. Coupling scheme
2. Map function
3. CML object
4. Evolution and Analysis
+++
## Coupling Schemes
Each coupling scheme requires a `couple()` function, with
- input: the lattice in its previous state
- output: the lattice in its updated state
This may require sub-functions. For example,
+++
### Two-Neighbor Coupling
---?code=couplings.py
@[7](Classic two-neighbor coupling scheme)
@[8-10](Requires a coupling strength and a Map object)
@[11]((Which determines the map function used))
@[19-33](The overarching coupling function)
@[13-14](Delegate function for updating lattice boundaries)
@[16-17](Delegate function for updating internal lattice cells)
