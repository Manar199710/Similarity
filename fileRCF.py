# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 11:49:00 2020

@author: hp
"""
'''
import numpy as np
file = open("EncodeAcide.txt","r")
contenu=file.read()
print(contenu)

for i in range(0,len(contenu)):
    if contenu[i]!=' ':
        if contenu[i]!='\n':
            T[k][int(contenu[i])]=1
        else:
            k=k+1
            
print(T)

'''
import csv

with open('EncodeAcide-TableEntier.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(" ") for line in stripped if line)
    with open('EncodeAcide-TableEntier.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('objet1', 'objet2','objet3', 'objet4','objet5', 'objet6','objet7', 'objet8','objet9','objet10', 'objet11','objet12', 'objet13','objet14', 'objet15','objet16'))
        writer.writerows(lines)
        
import pandas as pd 
import numpy as np
T = np.zeros((34,122))
k=0
data=pd.DataFrame(pd.read_csv("EncodeAcide-TableEntier.csv"))
data.fillna(0, inplace=True)
for i in range (len(data)):
    for j in data.columns:
        if data[j][i]!= 0 :
            T[k][int(data[j][i])-1]=1
        else :
            pass
    k=k+1

print(T)
np.savetxt('TatbleEntier-rcf.txt', T, fmt='%d')
    