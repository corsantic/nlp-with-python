# -*- coding: utf-8 -*-
import re

X = ["This is a wolf #scary",
     "Welcome to the jungle #missing",
     "113222 the number to know",
     "Remember the name s - John",
     "I                Love     You "]


    
    
for i in range(len(X)):
    X[i] = re.sub(r"\W"," ", X[i])
    X[i] = re.sub(r"\d"," ",X[i])
    X[i] = re.sub(r"\s+[a-z]\s+"," ",X[i],flags=re.I)
    X[i] = re.sub(r"\s+"," ",X[i])
    X[i] = re.sub(r"^\s","",X[i])
    X[i] = re.sub(r"\s$","",X[i])