import spacy
import spacy.displacy as displacy
import re

def udd_get_named_entities(text, keyword):
  nlp = spacy.load("en_core_web_lg")
  doc = nlp(text)
  result = []
  keyList = {'language': 'LANGUAGE', 'nationality': 'NORP', 'religion': 'NORP'}
  for ent in doc.ents:
    if (ent.label_ in keyList[keyword]) and ("".join(ent.text.split()).isalpha()):
      result.append(ent.text)
  return result

udd_get_named_entities('This is an english language and I am american and I am an Hindu', 'language')


https://gist.github.com/joshuabaker/d2775b5ada7d1601bcd7b31cb4081981
  
  
https://github.com/Dinuks/country-nationality-list/blob/master/countries.json

  
Atheism/Agnosticism
Bahá’í
Buddhism
Christianity
Confucianism
Druze
Gnosticism
Hinduism
Islam
Jainism
Judaism
Rastafarianism
Shinto
Sikhism
Zoroastrianism
Traditional African Religions
African Diaspora Religions
Indigenous American Religions



pip install -U git+https://github.com/aboSamoor/polyglot.git@master
