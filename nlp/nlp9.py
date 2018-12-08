
# N-gram Word

import random

#Sample data

# Sample data
text = """Oyuncu Meral Kaplan, geçtiğimiz yıl bebeğinin bakıcısı darafından darp edildiğini söyleyerek şikayetçi olmuştu. Olayın ardından dün Kaplan'ın darp edildiği değil şiddet uyguladığı ve sinir krizi geçirdiği iddia edilen görüntüler ortaya çıktı. Olaydan sonra Kanal D ekranlarında yayınlanan 2. Sayfa programına konuk olan Kaplan, ablasına ve annesine kesinlikle vurmadığını görüntülerde sinir krizi geçirdiğini anlattı."""

# TriGram
n = 6

ngrams = {}

# Create the n-grams


for i in range(len(text)-n):
    gram = text[i:i+n]
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n]) # text[0+3] = text[3] = b

# Testing our N-Gram model
    
currentGram = text[0:n]

result = currentGram

for i in range(500):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += nextItem
    currentGram = result[len(result)-n:len(result)]
    
print (result)