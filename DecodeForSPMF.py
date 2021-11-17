# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:30:20 2020

@author: hp
"""

# Usage
# python DecodeAfterSPMF.py fich-a-decoder fich-resultat
#
import sys
import pickle
import re

def decode(a):
#    print invdico
    list=a.split(' ')
    s=""
 #   print list
    for i in list:
 #       print "xxx"+i+"xxxx"
        if i!='' and int(i) in invdico.keys():
 #           print "oui"
            s=s+invdico[int(i)]+' '
            #print (invdico[int(i)])
 #   print s
    return s
results ='Res-CloseSPMF.txt'
#results= 'Res_ClosedAssociation rules.txt'
f = open(results,'r')
p=len(sys.argv)
print (p)

if p==3:
    f_out=sys.argv[2]
else:
    f_out="res_decode.txt"
res=open(f_out,'w')

    
# Construction du dictionnaire
dic = open('invdico.dbm', 'rb')
invdico = pickle.load(dic)
#nblig = pickle.load(dic)
dic.close()

#print "Nombre d'individus : "+str(nblig)

#print invdico
valsup=re.compile(r"SUP: ([0-9]*)$")
tiret=re.compile(r"\_")

        


for l in f.readlines():
    #print l
    l=l.rstrip()
    r=l.split("#")
    #print r
    aa=r[0].split('==> ') # on decoupe comme s'il s'agit d'une regle
    t=tiret.search(l)
    if not t:
        if len(aa)==1:
            rdec=decode(aa[0])
            #print r[1]
            p=valsup.search(r[1])
            if p :
                sv=p.group(1)
                #srel=int(sv)*100.0/nblig*1.0
                #res.write(rdec+'#SUP: '+sv+' #'+str(srel)+'%\n')
                res.write(rdec+' #SUP: '+sv+'\n')
        elif len(aa)==2:
            rdec0=decode(aa[0])
            rdec1=decode(aa[1])
            res.write(rdec0 +'==> '+ rdec1 +'# '+'# '.join(r[1:])+'\n')
        else:
            print('!!!!! ligne non conforme')
    #else:
        #print "non traite"
        #print l


res.close()
    
    
