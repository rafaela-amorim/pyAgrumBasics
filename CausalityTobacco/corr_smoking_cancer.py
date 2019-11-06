# This example is from the causality examples notebook -- causality tobacco

from IPython.display import display, Math, Latex, HTML
import pyAgrum as gum
import pyAgrum.lib.notebook as gnb
import pyAgrum.causal as csl
import pyAgrum.causal.notebook as cslnb

obs = gum.fastBN("smoking->cancer")

obs.cpt("smoking")[:] = [0.6, 0.4]
obs.cpt("cancer")[{"smoking":0}] = [0.9, 0.1]
obs.cpt("cancer")[{"smoking":1}] = [0.7, 0.3]

# gnb.sideBySide(obs, obs("smoking") * obs("cancer"))

obs.cpt("cancer")
obs.cpt("smoking")
obs.cpt("smoking") * obs.cpt("cancer")      # the joint distribution of smoking and cancer