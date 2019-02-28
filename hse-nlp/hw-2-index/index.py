import argparse
import pandas as pd
import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pymystem3 import Mystem

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('input', type = str, help = "JSON with Rambler news")
parser.add_argument('query', type = str, help = "Query to find similar news")
parser.add_argument('-l', '--lemmatize', action='store_true', help='Use lemmatization')
parser.add_argument('-g', '--ngrams', action='store_true', help='Use ngrams')
parser.add_argument("-o", "--output", type = int, default = 3, help = 'Numbers of docs to show')
args = parser.parse_args()
                    
data = []
with open('../hw-1-parser/output/rambler-news.json') as file:
    for line in file:
        data.append(json.loads(line))

data = pd.DataFrame(data)
data = data['text']

if args.ngrams:
    vectorizer = TfidfVectorizer(ngram_range=(1,2))
else:
    vectorizer = TfidfVectorizer()

if args.lemmatize:
    m = Mystem()
    tf_idf = vectorizer.fit_transform(data.map(lambda text:''.join(m.lemmatize(text))))
    tf_idf_query = vectorizer.transform([''.join(m.lemmatize(args.query))])
else:
    tf_idf = vectorizer.fit_transform(data)
    tf_idf_query = vectorizer.transform([args.query])

results = cosine_similarity(tf_idf_query, tf_idf)[0]
sort_args = np.argsort(results)[::-1]

for _, arg in enumerate(sort_args[:args.output]):
    print('Result #{}\n{}\n Cosine similarity = {}'.format(_ + 1,data[arg], results[arg]))