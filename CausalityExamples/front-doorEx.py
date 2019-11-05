# Front-door example from the "causality examples notebook"

from IPython.display import display, Math, Latex, HTML

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

mod = gum.BayesNet()
mod.add(gum.LabelizedVariable("smoking"))
mod.add(gum.LabelizedVariable("tar"))
mod.add(gum.LabelizedVariable("cancer"))

mod.addArc(0, 1)    # smoking -> tar -> cancer; smoking -> cancer
mod.addArc(1, 2)
mod.addArc(0, 2)

# Smoking
mod.cpt(0)[:] = [0.5, 0.5]

# Tar deposits
mod.cpt(1)[:] = [0.4, 0.6], [0.3, 0.6]

# Lung Cancer
mod.cpt(2)[{"smoking":0, "tar":0}] = [0.1, 0.9]
mod.cpt(2)[{"smoking":0, "tar":1}] = [0.15, 0.85]
mod.cpt(2)[{"smoking":1, "tar":0}] = [0.2, 0.8]
mod.cpt(2)[{"smoking":1, "tar":1}] = [0.25, 0.75]

d = csl.CausalModel(mod, [("Genotype", ["smoking", "cancer"])], False)  # False == do not keep arcs
cslnb.showCausalModel(d)


try:
    a = csl.doCalculusWithObservation (d, "cancer", {"smoking"})    
except csl.HedgeException as h:
    print (h.message)


# the variable "a" shows us the front-door adjustment formula for smoking causes lung cancer
display(Math(a.toLatex()))

