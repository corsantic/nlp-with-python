# -*- coding: utf-8 -*-
import re


sentence = "1996 was the year i born"


re.match(r"[a-zA-Z]+",sentence)


re.search(r"[a-zA-Z]+",sentence)


# Starts with

if re.match(r"^1996",sentence):
    print("Match")
else:
    print("No Match")
        
    
    
# Ends With
    
    
if re.search(r"born$",sentence):
    print("Match")
else:
    print("No Match")
        
    