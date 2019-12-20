from IPython.display import display, Math, Latex, HTML

import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

# Example from pages 42 to 44

# Two honest coins are tossed;
# The bell rings if at least one of the coins is Heads;
# You can't hear the bell, you have to rely on a witness who is somewhat unreliable;
# Whenever the bell doesn't ring there's an 50% chance that our witness will falsely report that it did.


bn = gum.fastBN("first->bell<-second;bell->witness")

# coin = 0: heads       coin = 1: tails
bn.cpt("first") = [1/2, 1/2]
bn.cpt("second") = [1/2, 1/2]

bn.cpt("witness")[{"bell": 1}] = [0, 1]         # the bell rang, so the witness definitely is gonna report it.
bn.cpt("witness")[{"bell": 0}] = [1/2, 1/2]     # it the bell didn't ring, then there's 50% chance that the witness will report as if it rang.

# 00 is heads heads, 11 is tails tails
bn.cpt("bell")[{"first": 0, "second": 0}] = [0, 1]
bn.cpt("bell")[{"first": 0, "second": 1}] = [0, 1]
bn.cpt("bell")[{"first": 1, "second": 0}] = [0, 1]
bn.cpt("bell")[{"first": 1, "second": 1}] = [1, 0]