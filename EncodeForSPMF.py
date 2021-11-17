#
# Usage : python <File-to-encode> <encoded-file>
# Usage : python <File-to-encode> (ecriture dans out.txt)
#
#

import sys
import pickle
import os
import subprocess
import time
import re
import datetime

p=len(sys.argv)

if p==3:
    f_out=sys.argv[2]
else:
    f_out="EncodeAcide_table entier.txt"

# Construction du dictionnaire
dico={}
invdico={}
indice=1
f=open('acide.txt','r')
for line in f.readlines():
    line=line.rstrip()
    #print(line)
    for i,e in enumerate(line.split(',')):
        a="T"+"-"+e
        if a not in dico.keys():
            dico[a]=indice
            invdico[indice]=a
            indice +=1
f.close()

print(dico)

# construction du fichier de donnees
out=open(f_out,'w')
f=open('acide.txt','r')
for line in f.readlines():
    line=line.rstrip()
    l=[]
    for i,e in enumerate(line.split(',')):
        a="T"+"-"+e
        l.append(dico[a])
    l.sort()
    l2=[str(i) for i in l]
    
    
#    input("xxx :")
#    out.write
    #out.write("{"+",".join(l2)+"}")
    out.write(" ".join(l2))
    out.write("\n")
f.close()
out.close()

fichier=open('invdico.dbm', 'wb')
pickle.dump(invdico,fichier)
