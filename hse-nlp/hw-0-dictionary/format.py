import json
import argparse
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from pymystem3 import Mystem

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('input', type = str, help = "JSON with Rambler news")
parser.add_argument("--dict", type = str, default = 'dictionary.json', help = "Dictionary output")
parser.add_argument('-l', '--lemmatize', action='store_true', help='Use lemmatization')

args = parser.parse_args()
                    
data = []
with open(args.input) as file:
    for line in file:
        data.append(json.loads(line))

data = pd.DataFrame(data)

if args.lemmatize:
	m = Mystem()
	data['title'] = data['title'].map(lambda text: ''.join(m.lemmatize(text)))
	data['text'] = data['text'].map(lambda text:''.join(m.lemmatize(text)))

vectorizer = CountVectorizer()
vectorizer.fit(data['title'].append(data['text']))

inverse_vocabulary = {str(v): k for k, v in vectorizer.vocabulary_.items()}

with open(args.dict,'w') as file:
    file.write(json.dumps(inverse_vocabulary,ensure_ascii=False,indent=1))