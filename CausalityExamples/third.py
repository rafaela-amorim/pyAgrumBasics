# example from the book -- page 66 - 68

from IPython.display import display, Math, Latex, HTML

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

# Smoking causes cancer?

# s is smoking, t is tar deposits, c is lung cancer
bn = gum.fastBN("smoking->tar->cancer")

# conditional probabilities table
bn.cpt('smoking')[:] = [0.5, 0.5]

bn.cpt('tar')[{'smoking':0}] = [380/400, 20/400]
bn.cpt('tar')[{'smoking':1}] = [20/400, 380/400]

bn.cpt('cancer')[{'smoking':0, 'tar':0}] = [38/380, 342/380]
bn.cpt('cancer')[{'smoking':0, 'tar':1}] = [1/20, 19/20]
bn.cpt('cancer')[{'smoking':1, 'tar':0}] = [18/20, 2/20]
bn.cpt('cancer')[{'smoking':1, 'tar':1}] = [323/380, 57/380]

# bn
# bn.cpt('cancer')

# Causal Model

d = csl.CausalModel(bn, [('genes', ['smoking', 'cancer'])])

cslnb.showCausalImpact(d, 'cancer', 'smoking', values={'smoking':1})
cslnb.showCausalImpact(d, 'cancer', 'smoking', values={'smoking':0})


# ci = csl.causalImpact(d, "cancer", "smoking", "", {'smoking': 1})
# display(Math(ci.toLatex()))

do = csl.doCalculusWithObservation (d, "cancer", "smoking", )