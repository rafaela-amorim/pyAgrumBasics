# this example comes from:
# http://www-desir.lip6.fr/~phw/aGrUM/docs/last/notebooks/01-tutorial.ipynb.html

%matplotlib inline
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

#   Create the probability tables   #

# Conditional Probabilities Table (CPT)
bn.cpt(c).fillWith([0.5,0.5])

# fill different columns - 1st form
bn.cpt(s)[:] = [ [0.5, 0.5], [0.9, 0.1] ]
# 2nd form
bn.cpt(s)[0,:] = 0.5      # equivalent to [0.5, 0.5]
bn.cpt(s)[1,:] = [0.9, 0.1]

# Returns an array with the parent nodes, and the last position is the node in the parameter
bn.cpt(s).var_names

bn.cpt(w).var_names     # [r, s, w]
bn.cpt(w)[0,0,:] = [1, 0]     # when r=0, s=0
bn.cpt(w)[0,1,:] = [0.1, 0.9]      # r=0, s=1
bn.cpt(w)[1,0,:] = [0.1, 0.9]      # r=1, s=0
bn.cpt(w)[1,1,:] = [0.01, 0.99]    # r=1, s=1

# use dictionaries to introduce data!!  -- it facilitates and avoids common errors

bn.cpt(r)[{'c': 0}] = [0.8, 0.2]
bn.cpt(r)[{'c': 1}] = [0.2, 0.8]
# use the name (string) of the variable 'c' , do not use the variable itself c (it won't work)

#   NOW YOUR BN IS COMPLETE!!   #   

# ------------------------------------------

# formats that we can save our bayesian network
# print(gum.availableBNExts())
# out: bif|dsl|net|bifxml|o3prm|uai

# Saving the BN in an archive 

# gum.saveBN(bn, os.path.join("out","WaterSprinkler.bif"))
gum.saveBN(bn, "WaterSprinkler.bif")

# Loading a BN from an archive
bn2 = gum.loadBN("WaterSprinkler.bif")

