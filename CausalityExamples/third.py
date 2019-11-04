# example from the book -- page 66 - 68

from IPython.display import display, Math, Latex, HTML

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

# Smoking causes cancer?

# s is smoking, t is tar deposits, c is lung cancer
bn = gum.fastBN("s->t->c")

# conditional probabilities table
bn.cpt('s')[:] = [0.5, 0.5]

bn.cpt('t')[{'s':0}] = [380/400, 20/400]
bn.cpt('t')[{'s':1}] = [20/400, 380/400]

bn.cpt('c')[{'s':0, 't':0}] = [38/380, 342/380]
bn.cpt('c')[{'s':0, 't':1}] = [1/20, 19/20]
bn.cpt('c')[{'s':1, 't':0}] = [18/20, 2/20]
bn.cpt('c')[{'s':1, 't':1}] = [323/380, 57/380]

# bn
# bn.cpt('c')

# Causal Model

# g is genes
d = csl.CausalModel(bn, [('g', ['s', 'c'])])

cslnb.showCausalImpact(d, 'c', 's', values={'s':1})
cslnb.showCausalImpact(d, 'c', 's', values={'s':0})

do_s0 = csl.causalImpact(d, 'c', 's', '', {'s':0})
do_s1 = csl.causalImpact(d, 'c', 's', '', {'s':1})