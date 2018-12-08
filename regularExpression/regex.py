# -*- coding: utf-8 -*-

import re


sentence = "I was born in the year 1996"
sentence = "ab"

re.match(r".*",sentence) # Zero or more means *
re.match(r".+",sentence) # 1 or more means +
re.match(r"[a-zA-Z]+",sentence)

re.match(r"ab?",sentence)
