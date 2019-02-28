Collect news data from Rambler.

## Dependencies

Install Dependencies via ```pip3 install -r requirements.txt```  

Install [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

* beautifulsoup4==4.6.0
* requests==2.18.4
* html2text==2018.1.9
* pandas==0.20.3
* pymystem3==0.1.9
* selenium==3.8.1
* tqdm==4.19.5
* scikit_learn==0.19.1
* atlas==0.27.0

## Usage

### Parse Rambler News links

```
usage: parse-rambler-links.py [-h] [-o OUTPUT] category pages

positional arguments:
  category              Category, e.g. [politics], [economics], [tech],
                        [starlife]
  pages                 Number of Pages to parse

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        File to write links
```

Example: `python3 parse-rambler-links.py tech 35`

### Parse Rambler News from JSON links.

```
usage: parse-rambler-news.py [-h] [-s START] [-t TIMEOUT] [-e END] [-o OUTPUT]
                             input

positional arguments:
  input                 File with links

optional arguments:
  -h, --help            show this help message and exit
  -s START, --start START
                        The line number to start with
  -t TIMEOUT, --timeout TIMEOUT
                        TimeOut value
  -e END, --end END     The line number to stop with
  -o OUTPUT, --output OUTPUT
                        File to write news
```

Example: `python3 parse-rambler-news.py output/rambler-news-links.json`

### Format news to JSON and XML (BoW with dictionary JSON)

```
usage: format.py [-h] [--json JSON] [--xml XML] [--dict DICT] [-l] input

positional arguments:
  input            JSON with Rambler news

optional arguments:
  -h, --help       show this help message and exit
  --json JSON      JSON BoW output
  --xml XML        XML BoW output
  --dict DICT      Dictionary output
  -l, --lemmatize  Use lemmatization
```

Example: `python3 format.py output/rambler-news.json --lemmatize`

## Examples
* JSON per line

### rampler-news-links.json

```
{
  "link": "https://news.rambler.ru/politics/39054690-pushkov-prokommentiroval-trebovaniya-ukrainy-reformirovat-sovbez-oon/", 
  "category": "politics"
}
```

### rampler-news.json

```
{
  "link": "https://news.rambler.ru/politics/39054690-pushkov-prokommentiroval-trebovaniya-ukrainy-reformirovat-sovbez-oon/", 
  "category": "politics", 
  "title": "Пушков назвал требования Украины лишить РФ права на вето глупой затеей", 
  "text": "Член Совета Федерации РФ Алексей Пушков назвал требования Украины реформировать СБ ООН, чтобы лишить Россию права 
    вето, глупой и безнадежной затеей. По его словам, украинским дипломатам никто не даст поставить под сомнение особую 
    прерогативу великих держав, передает РИА Новости.
    Делегация Украины в ООН потребовала реформировать Совет Безопасности 
    организации, изменив процедуры применения права вето. 
    В Киеве не раз заявляли о необходимости лишить Москву права вето в международной организации. 
    А министр иностранных дел Украины Павел Климкин называл постоянное членство России в Совбезе ООН «фундаментальной проблемой»."
}
```

### bow.json

```
{ 
  "category": "politics", 
  "link": "https://news.rambler.ru/politics/39054690-pushkov-prokommentiroval-trebovaniya-ukrainy-reformirovat-sovbez-oon/", 
  "sentence": [
    [2565, 3464, 4790, 7272, 11095, 15282, 17315, 20497, 25333, 27913, 29459, 29755, 29945, 30257, 31780, 34682, 35485, 36410, 37595, 37626], 
    [4626, 8045, 8464, 8704, 9686, 18097, 19000, 19097, 21051, 22490, 23194, 23429, 24945, 25979, 29523, 31311, 32062, 35467], 
    [3476, 4790, 8332, 11783, 20497, 20808, 25201, 25333, 26419, 27684, 29459, 31779, 35485], 
    [4790, 11240, 13229, 15282, 16047, 16917, 18097, 18516, 20808, 25333, 28117], 
    [8308, 12141, 13392, 16429, 17367, 20497, 21991, 25013, 26824, 29739, 31739, 35485, 36780, 37605]
  ], 
  "title": [[4790, 7272, 11095, 15282, 17143, 17315, 25333, 27913, 29945, 34682, 35485]]}
```

### bow.xml

```
<all>
  <category>politics</category>
  <link>https://news.rambler.ru/politics/39054690-pushkov-prokommentiroval-trebovaniya-ukrainy-reformirovat-sovbez-oon/</link>
  <sentence> 2565 3464 4790 7272 11095 15282 17315 20497 25333 27913 29459 29755 29945 30257 31780 34682 35485 36410 37595 37626</sentence>
  <sentence> 4626 8045 8464 8704 9686 18097 19000 19097 21051 22490 23194 23429 24945 25979 29523 31311 32062 35467</sentence>
...
</all>
```

### dictionary.json

```
{
 "27913": "пушков",
 "17315": "назвал",
 "34682": "требования",
 "35485": "украины",
 "15282": "лишить",
...
}
```

## Jupyter Notebook

See *report.ipnb* for more details.

## Others

* `output/` - All collected data is available here.
