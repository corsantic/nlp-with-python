# -*- coding: utf-8 -*-

import nltk
from nltk.stem import PorterStemmer as ps


paragraph ="""Ciao, I am Leonardo Da Vinci one of the world's greatest artists of all time. 
I was born on 1452 which means I was one of the many people to have lived in the time of the renaissance.
 Most of you may know two of my most famous paintings which would be "The Mona Lisa" ,and "The Last Supper".
 As a little kid I would venture my small village of Vinci where I had learnt many thinga. 
 For I was always allowed to go to the woods and observe animal, plants , and any other thing I could find.
 When I would go out to observe things I would always have a sketch pad ,
 or note pad to sketch and write down things I would learn, find, and see.
 When I was twelve me and my dad ,Sir Piero Da Vinci, 
 who was a notary moved from my home village Vinci to Florence,
 Italy. My mom who was a peasant had not come with us for she had left my father to raise me alone. 
 When we moved my dad apprenticed me to an artist named Verrocchio. 
 As I got older and more skilled at painting Verrocchio would let me work on some of the paintings with him.
 Verrocchio and me would sometimes have to make very important paintings for important people.
 All the years that I was apprenticed to him had helped me to become a better painter.
 After my apprenticeship to Verrocchio was over I keep on painting and I moved around from place to place all over Italy and some of France painting and inventing things.
 I had opened a small studio where I would take pupils under my apprenticeship and teach them how to learn the arts of painting as Verrocchio did to me.
 After I had stopped working on the studio. Since i did not go to the studio anymore I had time to make sketchs ,
 and blueprints for many inventions that you have today like a bicycle, a flying machine or helicopter how ever you would call it , and armored cars. I had many other inventions which were not shown to the world til much after they were made. 
When I had moved to France I had became friend with the duke of France and I had also started working for the Duke, helping him improve his army by inventing things for him and his army. I would build him things such as tanks and machine guns which I believe helped his army a lot. I have been making art for many years and just as I did as a child I have also been observing thing as they evolve, and here I am teaching you about me and also observing you all for you have all evolve and you all know many things I do not."""
 
 
sentences = nltk.sent_tokenize(paragraph)
 
stemmer = ps()
 
 
 # Stemming
 
for i in range(len(sentences)):
     words = nltk.word_tokenize(sentences[i])
     newWords = [stemmer.stem(word) for  word in words]
     sentences[i] = ' '.join(newWords)