# This example is from the book --- Causal Inference in Statistics: A Primer
# page 62, figure 3.6

from IPython.display import display, Math, Latex, HTML

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

bn = gum.fastBN("x->y<-w")

# -- conditional probabilities table
bn.cpt('w')[:] = [0.7, 0.3]

bn.cpt('x')[:] = [0.4, 0.6]

bn.cpt('y')[{'x':0, 'w':0}] = [0.2, 0.8]
bn.cpt('y')[{'x':0, 'w':1}] = [0.1, 0.9]
bn.cpt('y')[{'x':1, 'w':0}] = [0.9, 0.1]
bn.cpt('y')[{'x':1, 'w':0}] = [0.5, 0.5]


# ** making the Causal Model

d = csl.CausalModel(bn, [('z', ['x', 'w'])])

cslnb.showCausalImpact(d, 'y', 'x', values={'x':0})
cslnb.showCausalImpact(d, 'y', 'x', values={'x':1})