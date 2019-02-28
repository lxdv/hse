Make BoW dictionary from corpus.

## Dependencies

Install Dependencies via ```pip3 install -r requirements.txt```

* pymystem3==0.1.9
* pandas==0.20.3
* scikit_learn==0.19.1

## Usage

```
usage: format.py [-h] [--dict DICT] [-l] input

positional arguments:
  input            JSON with Rambler news

optional arguments:
  -h, --help       show this help message and exit
  --dict DICT      Dictionary output
  -l, --lemmatize  Use lemmatization
```

Example: ```python3 format.py corpus.json --lemmatize```

## Example

dictionary.json

```
{
 "12928": "пушок",
 "8939": "называть",
 "15736": "требование",
 "16067": "украина",
 "7892": "лишать",
 "13773": "рф",
 "12093": "право",
 "8842": "на",
 "3420": "вето",
 "4420": "глупый",
...
}
```

## Jupyter Notebook

See *report.ipnb* for more details.