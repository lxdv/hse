import json
import requests
from bs4 import BeautifulSoup
from html2text import html2text
import tqdm
import argparse
from time import sleep

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('input', type = str, help = "File with links")
parser.add_argument("-s", "--start", type = int, default = 0, help = 'The line number to start with')
parser.add_argument("-t", "--timeout", type = int, default = 1, help = 'TimeOut value')
parser.add_argument('-e', "--end", type=int, help="The line number to stop with")
parser.add_argument("-o", "--output", type = str, default = 'rambler-news.json', help = "File to write news")
args = parser.parse_args()
                    
posts = []
with open(args.input) as file:
    for line in file:
        posts.append(json.loads(line))
if args.end == None:
    args.end = len(posts)

posts = posts[args.start:args.end]

for element in tqdm.tqdm(posts):
	try:
	    soup = BeautifulSoup(requests.get(element['link']).text, "lxml")
	    title = html2text(soup.findAll('h1',attrs={'class': 'big-title__title'})[0].text).replace('\n', '')
	    text = ''
	    for paragraph in soup.findAll('div',attrs={'class': 'article__paragraph'}):
	        text += html2text(paragraph.text).replace('\n', ' ') + ' '
	        
	    with open(args.output,'a') as file:
	                    file.write(json.dumps({
	                        'link' : element['link'],
	                        'category': element['category'],
	                        'title': title,
	                        'text': text
	                    },ensure_ascii=False) + '\n')
	except:
		print('Error with link - ', element['link'])
		pass

	sleep(args.timeout)