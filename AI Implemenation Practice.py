# AI Practice
import spacy

nlp = spacy.load("en_core_web_sm")

#Example text
text = "Natural language processing is a fascinating field of study."

#Process the text using spaCy
doc = nlp(text)

#Acess token-lovel info
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}, Tag: {token.tag_}")

#Extract named entities
for ent in doc.ents:
    print(f"Entity: {ent.text}, Label: {ent.label_}")