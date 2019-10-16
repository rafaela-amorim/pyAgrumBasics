from IPython.display import display, Math, Latex, HTML

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

bn = gum.fastBN("w->x->z->y;w->z")

# conditional probabilities tables
bn.cpt("w")[:] = [0.7, 0.3]
                
#                w = 0         w = 1
bn.cpt("x")[:] = [0.4, 0.6], [0.3, 0.7]

bn.cpt('z')[{'w':0, 'x':0}] = [0.2, 0.8]
bn.cpt('z')[{'w':0, 'x':1}] = [0.1, 0.9]
bn.cpt('z')[{'w':1, 'x':0}] = [0.9, 0.1]
bn.cpt('z')[{'w':1, 'x':1}] = [0.5, 0.5]

#                   z = 0       z = 1
bn.cpt('y')[:] = [0.1, 0.9], [0.8, 0.2]

d = csl.CausalModel(bn, [("lat1", ['x', 'y'])] )    # ???????????????
# csl.causalImpact(d, "y", {"x":0})
# O Impacto causal de x em y quando intervimos em x e dizemos que x = 0

cslnb.showCausalImpact(d, "y", "x", values={"x":0})
cslnb.showCausalImpact(d, "y", "x", values={"x":1})