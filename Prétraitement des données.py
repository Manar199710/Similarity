# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import pandas as pd 
import numpy as np

data=pd.DataFrame(pd.read_excel("Acide sinapique.xlsx"))
data=data.drop(columns=['Conc Utilisées'])
np.savetxt('acide.txt',data.values, fmt='%s', delimiter=",")
