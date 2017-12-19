# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:54:45 2017

@author: crist
"""

# Funciones:


def n_elementos_pos(l):
    acum = 0
    for i in l:
        if i>0 :
            acum +=2
        else:
            acum += 1
    return acum   



def suma_saltando(l,i,n):
    acum= 0
    for i in l[i: 3 : n]:
        acum += i
    return acum 


def divisores(x):
    res= []
    for i in range(1,x//2):
        if x % i== 0:
            res.append(i)
    return res  

def covarianza(l,m):
    medial=sum(l)/len(l)
    mediam=sum(m)/len(m)
    n=len(l)
    acum=0
    for i,j in zip(l,m):
        acum +=((i-medial)*(j-mediam))/n
    return acum  
