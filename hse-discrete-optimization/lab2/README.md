## Lab 2: Max clique using branching and Max Clique

### Dependencies

- Python 3.6
- CPLEX library *(academic version only)*
- *Jupyter Notebook (if you want to use it)*


### Usage

1. You can find max clique by running `main.py` from your terminal.

```
usage: main.py [-h] [--no_multy] filename

positional arguments:
  filename    File with graph

optional arguments:
  -h, --help  show this help message and exit
  --no_multy  Turn off multiprocessing
```

Example:
`python main.py /Users/lxdv/Desktop/lab2/dimacs-files/hamming6-2.clq `
```
Max clique: 32
Time: 501 ms
```
  
2. You can also find max clique by running code in jupyter notebook. *(if you want to use it)*

### Results 

Instance|Nodes|Edges|Best known|Found by our algorithm|Time (ms)
---|---|---|---|---|---
hamming6-4.clq|64|704|4|4|1419
hamming6-2.clq|64|1824|32|32|370
hamming8-4.clq|256|20864|16|16|1034637
johnson8-2-4.clq|28|210|4|4|94
johnson8-4-4.clq|70|1855|14|14|644
johnson16-2-4.clq|120|5460|8|8|1038
MANN_a9.clq|45|918|16|16|295
san200_0.7_1.clq|200|13930|30|30|83204
san200_0.7_2.clq|200|13930|18|18|623280
san200_0.9_1.clq|200|17910|70|70|1889
san200_0.9_2.clq|200|17910|60|60|2061
C125.9.clq|125|6963|34|34|84493007
c-fat200-1.clq|200|1534|12|12|22345
c-fat200-2.clq|200|3235|24|24|1061
c-fat200-5.clq|200|8473|58|58|30990
c-fat500-2.clq|500|9139|26|26|7798
c-fat500-5.clq|500|23191|64|64|142082
