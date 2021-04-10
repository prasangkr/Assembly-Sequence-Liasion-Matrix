# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 20:30:14 2021

@author: lenovo
"""
import pandas as pd
#wirte the path of your csv file
orgtable= pd.read_csv('dfmalab\pythonas1.csv', header= None)
l1array=[]
for i in range(orgtable.shape[1]):
    for j in range(orgtable.shape[1]):
        if orgtable[i][j]==1:
            l1array.append((i+1,j+1))

l2array=[]
#l1 = pd.DataFrame(l2array) 
for a in range(orgtable.shape[1]-2):
       
    for x in range(len(l1array)):
        for y in range(orgtable.shape[-1]):
            if orgtable[(l1array[x][1]-1)][y]==1:
                if y+1 not in l1array[x]:
                    #print(l1array[x])
                    #print("l1")
                    l2array.append((l1array[x], y+1))# if y+1 in l1array[x]
                    #print(l2array)
                    print("sfhddddglllllllll")
    l1array = l2array
    l2array=[]
    
def flatten2list(object):
    gather = []
    for item in object:
        if isinstance(item, (list, tuple, set)):
            gather.extend(flatten2list(item))            
        else:
            gather.append(item)
    return gather
final=[]
for i in range(len(l1array)):
    res = flatten2list(l1array[i])
    final.append(res)
    
finalseq= []

for a in final:
    aset= set(a)
    if len(a) == len(aset):
        finalseq.append(a)
        