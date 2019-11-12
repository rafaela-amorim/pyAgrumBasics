from IPython.display import display, Math, Latex, HTML

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

bn = gum.fastBN("smoking->tar->cancer")

# -- conditional probabilities table --
bn.cpt("smoking")[:] = [0.5, 0.5]

bn.cpt("tar")[{"smoking":0}] = [380/400, 20/400]
bn.cpt("tar")[{"smoking":1}] = [20/400, 380/400]

bn.cpt("cancer")[{"tar":0, "smoking":0}] = [0.1, 0.9]
bn.cpt("cancer")[{"tar":0, "smoking":1}] = [0.9, 0.1]
bn.cpt("cancer")[{"tar":1, "smoking":0}] = [0.05, 0.95]
bn.cpt("cancer")[{"tar":1, "smoking":1}] = [0.85, 0.15]

d = csl.CausalModel(bn, [("genes", ["smoking", "cancer"])] )

cslnb.showCausalImpact(d, "cancer", "smoking", values={"smoking":1})
cslnb.showCausalImpact(d, "cancer", "smoking", values={"smoking":0})