from IPython.display import display, Math, Latex, HTML

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

bn = gum.fastBN("w->x->z->y;w->z")

# -- conditional probability tables
bn.cpt('w')[:] = [0.7, 0.3]

bn.cpt('x')[:] = [0.4, 0.6], [0.3, 0.7]

bn.cpt('z')[{'w':0, 'x':0}] = [0.2, 0.8]
bn.cpt('z')[{'w':0, 'x':1}] = [0.1, 0.9]
bn.cpt('z')[{'w':1, 'x':0}] = [0.9, 0.1]
bn.cpt('z')[{'w':1, 'x':1}] = [0.5, 0.5]

bn.cpt('y')[:] = [0.1, 0.9], [0.8, 0.2]


# **** Causal model plot ****

# d is a causal model! It receives a bayesian network and the unmeasured variables in it along
# with the variables that are affected by these latent variables

# -- "lat1" is an unmeasured variable that affects X and Y (its parent of both -- the common cause in the fork)
d = csl.CausalModel(bn, [("lat1", ['x', 'y'])])



# -- causal impact of X on Y when we do(X = 0)
# this works but the representation of the causal impact returned isn't very good
###### csl.causalImpact(d, 'y', 'x', '', {'x':0})    

# shows the causal impact of X on Y, when we do(X = 0), on the causal model D
cslnb.showCausalImpact(d, "y", "x", values={"x":0})

# causal impact of X on Y when do(X = 1), on causal model d
cslnb.showCausalImpact(d, "y", "x", values={"x":1})