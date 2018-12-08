# -*- coding: utf-8 -*-

import nltk
from nltk.corpus import stopwords

paragraph ="""TBMM “Türkçede Bozulma ve Yabancılaşmanın Araştırılması ve Türkçenin Korunması ve Etkin Kullanımı İçin Alınması Gereken önlemlerin Belirlenmesi” amacıyla bir Araştırma Komisyonu kurdu. Türkçe kirlendi, yozlaştı, öldü bitti feryatları göğe yükseldiği için doğrusu böyle bir gelişmede şaşılacak bir şey yok. Dile bu kadar ilgi gösterilmesi elbette sevindirici bir şey. Herhangi bir soruna çözümün komisyonlarda değil, bazen uzun yıllar sürebilecek ciddi, zahmetli, zaman zaman sinir bozucu araştırmalarla bulunabileceğini düşünen birisiyim. Yine de komisyonun yararlı bilgiler ortaya koymasını yürekten arzu ederim. Ne var ki komisyondan, epeyce taraftarı olan “Türkçe yozlaşıyor, kirleniyor, bozuluyor” vb. gibi bir sonucun ortaya çıkma olasılığı da yüksek.

Komisyona yardımcı olabilecek birkaç soru: Hem standart Türkçe hem de yabancı dil öğretiminde neden bu kadar başarısızız? insanlar,Türkçe kelime bulamadıkları için mi işyerlerine yabancı isimler veriyor? Neden dil konuları “ciddi” havasındaki programlarda bile şaşılası bir sığlıkla tartışılır? Türkiye’de satılan malların Türkçe açıklamaları olması için neler yapılmalıdır? Dil zaptiyeliği yapan dernekler, mesela Türkçe kılavuz kelimesini niçin klana biçiminde yazarlar? Türkiye’de üretilen bilgi yabancı dilde yayınlanırsa neden daha itibarlı olur? vb. vb. Soruları çoğaltmak mümkün, ama yazının asıl amacı o değil?"""
 

sentences = nltk.sent_tokenize(paragraph)

for i in range (len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    newWords = [word for word in words if word not in stopwords.words('turkish')]
    sentences[i] = ' '.join(newWords)