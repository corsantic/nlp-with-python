
import nltk

nltk.download()

paragraph ="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent imperdiet ultrices velit at eleifend. Nunc porttitor ex a justo viverra viverra.
 Mauris aliquam lacus et luctus pharetra. 
 Donec egestas volutpat neque eget blandit. 
 Praesent sed elit a odio vehicula mattis in at leo.
 Cras bibendum lacus vel luctus efficitur.
 Proin auctor purus nec posuere laoreet. 
 Nam sed lorem nec magna auctor bibendum.
 Praesent cursus nibh a facilisis lacinia.
 Ut dictum, purus at ultrices euismod, neque elit luctus lorem, 
 tristique tempus risus leo vitae libero. Cras dictum, elit ut hendrerit vehicula,
 massa nulla luctus lectus, ut venenatis nibh quam eu sapien.
 Morbi et est non eros fringilla sagittis. Etiam cursus ex in aliquet ultrices."""
 
sentences = nltk.sent_tokenize(paragraph)
 
 words = nltk.word_tokenize(paragraph)
 
 