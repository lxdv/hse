import sys
import networkx as nx

def parser(filename):
    G = nx.Graph()
    try:   
        with open(filename) as f:
            for line in f:
                if line.startswith("e"):
                    splitted_line = line.split(" ")
                    G.add_edge(int(splitted_line[1]), int(splitted_line[2]))              
        return(G) 
    except:
        print("No such file:", filename)
        sys.exit(1)