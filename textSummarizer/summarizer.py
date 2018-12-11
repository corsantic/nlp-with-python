
import bs4 as bs
import urllib.request
import re
import nltk
nltk.download('stopwords')

source = urllib.request.urlopen('https://www.bbc.com/news/technology-46516662')

soup  = bs.BeautifulSoup(source, 'lxml')

text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text


# Preprocessing the text
text = re.sub(r'Share this withEmailFacebookMessengerMessengerTwitterPinterestWhatsAppLinkedInCopy this linkThese are external links and will open in a new window',' ',text)
text = re.sub(r'\s+',' ',text)
clean_text = text.lower()
clean_text = re.sub(r'\W',' ',clean_text)
clean_text = re.sub(r'\d',' ',clean_text)
clean_text = re.sub(r'\s+',' ',clean_text)


sentences = nltk.sent_tokenize(text)

stop_words = nltk.corpus.stopwords.words('english')