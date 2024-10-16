import spacy
from pymorphy3 import MorphAnalyzer


nlp = spacy.load("ru_core_news_sm")
morph = MorphAnalyzer()


def extract_proper_nouns(text):
    doc = nlp(text)
    proper_nouns = []

    for token in doc:
        if token.pos_ == "PROPN":
            normalized = morph.parse(token.text)[0].normal_form
            proper_nouns.append(normalized)

    return proper_nouns


text = "Мария пошла в магазин, а Иван встретился с Дмитрием в Санкт Петербурге."
names = extract_proper_nouns(text)
print(names)
