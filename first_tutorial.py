# this example comes from:
# http://www-desir.lip6.fr/~phw/aGrUM/docs/last/notebooks/01-tutorial.ipynb.html

# %matplotlib inline
from pylab import *
import matplotlib.pyplot as plt
import os

import pyAgrum as gum
# import pyAgrum.lib.notebook as gnb

# create an empty Bayesian Network (BN)
bn = gum.BayesNet('WaterSprinkler')
print (bn)

# bernoulli variable to say if it's cloudy or not
c = bn.add(gum.LabelizedVariable('c', 'cloudy?', 2)) # name, label of the variable, how many values
# numeric id of c
print (c)

# more bernoulli variables
s = bn.add(gum.LabelizedVariable('s', 'sprinkler?', 2))
r = bn.add(gum.LabelizedVariable('r', 'raining?', 2))
w = bn.add(gum.LabelizedVariable('w', 'wet grass?', 2))
print (s,r,w)   # more numeric ids

# how the BN is now
print (bn)

#    Creating the arcs    #

print ("Now adding the edges:")
# directed edge from c to s
bn.addArc(c, s) 

for link in [(c,r), (s,w), (r,w)]:
    bn.addArc(*link)    # a pointer for the tuples in the array!!

print (bn)
import pyAgrum.lib.notebook as gnb
bn