import re


sentence = "You think you do but you don't"

print(re.sub(r"don't","do",sentence))



print(re.sub(r"[a-z]","0",sentence,1,flags = re.I))

print(re.sub(r"[a-z]","0",sentence,flags = re.I))
