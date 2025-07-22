# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 21:51:58 2018

@author: pranjal
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset =pd.read_csv('IMDB-Movie-Data.csv')
trainset=pd.read_csv('IMDB-Movie-Data-1.csv')

impdataset=dataset.iloc[:,[1,2,6,8,10,11]]
impdataset['Action']=0
impdataset['Comedy']=0
impdataset['Sci-Fi']=0
impdataset['Adventure']=0
impdataset['Drama']=0
impdataset['Horror']=0
impdataset['Thriller']=0
impdataset['Animation']=0
impdataset['Romance']=0
impdataset['Fantasy']=0
impdataset['Family']=0
impdataset['History']=0
impdataset['Biography']=0
impdataset['Music']=0
impdataset['Mystery']=0
impdataset['Crime']=0
index=0
l='Action'
a='Comedy'
b='Sci-Fi'
c='Adventure'
d='Drama'
e='Horror'
f='Thriller'
g='Animation'
h='Romance'
i='Fantasy'
j='Family'
k='History'
m='Biography'
n='Music'
o='Mystery'
z='Crime'
import array
p=array.array('f',[0])
while(index<1000):
    p.append(0)
    x=impdataset.loc[index].Genre.rfind(l)
    if(x!=-1):
        impdataset.loc[index,l]=impdataset.loc[index,l]+1
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(a)
    if(x!=-1):
        impdataset.loc[index,a]=impdataset.loc[index,a]+1   
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(b)
    if(x!=-1):
        impdataset.loc[index,b]=impdataset.loc[index,b]+1
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(c)
    if(x!=-1):
        impdataset.loc[index,c]=impdataset.loc[index,c]+1   
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(d)
    if(x!=-1):
        impdataset.loc[index,d]=impdataset.loc[index,d]+1
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(e)
    if(x!=-1):
        impdataset.loc[index,e]=impdataset.loc[index,e]+1   
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(f)
    if(x!=-1):
        impdataset.loc[index,f]=impdataset.loc[index,f]+1
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(g)
    if(x!=-1):
        impdataset.loc[index,g]=impdataset.loc[index,g]+1 
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(h)
    if(x!=-1):
        impdataset.loc[index,h]=impdataset.loc[index,h]+1
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(i)
    if(x!=-1):
        impdataset.loc[index,i]=impdataset.loc[index,i]+1  
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(j)
    if(x!=-1):
        impdataset.loc[index,j]=impdataset.loc[index,j]+1
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(k)
    if(x!=-1):
        impdataset.loc[index,k]=impdataset.loc[index,k]+1 
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(m)
    if(x!=-1):
        impdataset.loc[index,m]=impdataset.loc[index,m]+1
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(n)
    if(x!=-1):
        impdataset.loc[index,n]=impdataset.loc[index,n]+1   
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(o)
    if(x!=-1):
        impdataset.loc[index,o]=impdataset.loc[index,o]+1
        p[index]=p[index]+1
    x=impdataset.loc[index].Genre.rfind(z)
    if(x!=-1):
        impdataset.loc[index,z]=impdataset.loc[index,z]+1  
        p[index]=p[index]+1
    index=index+1
traindata=impdataset.iloc[[54,80,117,36,96,249,64,99,124,133],:]
traindata['Ratingbyme']=[9,9.7,8.5,9.2,7,8,8.2,9,9.5,8] 
for w in [54,80,117,36,96,249,64,99,124,133]:
   traindata.loc[w,'Ratingbyme']=traindata.loc[w,'Ratingbyme']*p[w]/3   
X=traindata.iloc[:,6:21].values
y=traindata.iloc[:,22].values
    
from sklearn.linear_model import LinearRegression 
regressor=LinearRegression()
regressor.fit(X,y)
    
impdataset['ratingbyme']=regressor.predict(impdataset.iloc[:,6:21])
traindata['ratingbyme1']=regressor.predict(X)
index=0
while(index<1000):
    f=float(impdataset.loc[index,'ratingbyme'])
    if(p[index]!=0):
      f=f/float(p[index])
    else:
      print(index)    
    impdataset.loc[index,'ratingbyme']=f*p[index]/3
    impdataset.loc[index,'finalscore']=impdataset.loc[index,'ratingbyme']*((40*impdataset.loc[index,'Rating'])+impdataset.loc[index,'Metascore'])
    index=index+1
     
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    