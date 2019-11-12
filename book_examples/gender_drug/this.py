from IPython.display import display, Math, Latex, HTML

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

# example from the book -- page 2 chapter 1
# 700 patients, 350 took the drug and 350 didn't
# gender is being taken into account

bn = gum.fastBN("gender->recovery<-drug_take;gender->drug_take")

m = 357     # total of men in the experiment
w = 343     # total of women in the experiment



# there are 357 men and 343 women
# gender = 0 is man; gender = 1 is woman
bn.cpt("gender") = [0.51, 0.49]

# drug_take = 0 is no drugs, drug_take = 1 is drug (taken)
bn.cpt("drug_take")[{"gender":0}] = [270/m, 87/m]
bn.cpt("drug_take")[{"gender":1}] = [80/w, 263/w]

# still needs doing
bn.cpt("recovery")[{"gender":0, "drug_take":0}] = []
bn.cpt("recovery")[{"gender":0, "drug_take":1}] = []
bn.cpt("recovery")[{"gender":1, "drug_take":0}] = []
bn.cpt("recovery")[{"gender":1, "drug_take":1}] = []