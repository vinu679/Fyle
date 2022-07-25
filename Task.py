import spacy
import spacy.displacy as displacy
import re

def udd_get_nationalities_Spacy(text):
  ## Required Static Nationalities List
  nationalities = {'british','scottish','irish','welsh','danish','finnish',
                   'norwegian','swedish','swiss','estonian','latvian','lithuanian',
                   'austrian','belgian','french','german','italian','dutch',
                   'american','canadian','mexican','ukrainian','russian','belarusian',
                   'polish','czech','slovak','slovakian','hungarian','romanian','bulgarian','greek','spanish'}

  nlp = spacy.load("en_core_web_lg", disable=['parser', 'tagger', 'textcat', 'lemmatizer'])
  text = text.strip()
  text = re.sub("\s+", " ", text)

  if len(text) > 1000000:
    return []
  else:
    nlp.max_length = 1000000

  doc = nlp(text)
  result = list(set([ent.text.lower() for ent in doc.ents]).intersection(nationalities))

  return result;
