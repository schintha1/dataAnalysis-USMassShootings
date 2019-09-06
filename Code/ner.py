import nltk 
import pandas
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
debate_data = pandas.read_csv("shootings.csv")
df = debate_data['Summary'].apply(lambda x: ' '.join(x))
chunked_sentences = list()
chunked_sentence = list()
for frame in range(len(df)):
    sentences1 = nltk.sent_tokenize(df[frame])
    for sentence in sentences1:
        sentences = re.sub(' (?! )', '',sentence)
        tokenized_sentences = [nltk.word_tokenize(sentences)]
        for sentence in tokenized_sentences:
            tagged_sentences = [nltk.pos_tag(sentence)]
        chunked_sentence = list(nltk.ne_chunk_sents(tagged_sentences, binary=True))
        for sentence in chunked_sentence: 
            chunked_sentences.append(sentence)

def extract_entity_names(t):
    entity_names = []

    if hasattr(t, 'label') and t.label:
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

entity_names = []
for tree in chunked_sentences:

    entity_names.extend(extract_entity_names(tree))

print set(entity_names)
