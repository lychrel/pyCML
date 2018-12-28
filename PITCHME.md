@img[clip-img bg-black clean-img span-30](img/alpha_evolution.gif)
# @color[#f95e64](pyCML)
@color[#f95e64](For rapid construction and simulation of CMLs)
---
## Getting Started
1. Coupling scheme
2. Map function
3. CML object
4. Evolution and Analysis
---
## Coupling Schemes
Each coupling scheme requires a `couple()` function:
- input: the lattice in its previous state
- output: the lattice in its updated state
This may require sub-functions. For example,
+++?code=couplings.py&title=Two-Neighbor
@[7](Classic two-neighbor coupling scheme)
@[8-10](Requires a coupling strength and a Map object)
@[11]((Which determines the map function used))
@[19-33](The overarching coupling function)
@[13-14](Delegate function for updating lattice boundaries)
@[16-17](Delegate function for updating internal lattice cells)
---
## Map Functions
Each map requires a `_map()` function:
- input: a previous state
- output: the next state 
and parameter(s) `alpha`
---
### Kaneko Logistic Map
`\[
f(x) = 1 - \alpha x^{2}
\]`
+++?code=maps.py&title=Kaneko
@[5-11](General Map class)
@[8-11](Bifurcation Parameter getter/setters)
@[19-23](Kaneko logistic map class)
@[22-23](Map function updates previous state)

