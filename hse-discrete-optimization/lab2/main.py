import argparse
from clique import find_clique_multi
from clique import find_clique

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('filename', type = str, help = "File with graph")
parser.add_argument('--no_multy', action='store_false', help='Turn off multiprocessing')
args = parser.parse_args()

if args.no_multy:
	find_clique(args.filename)
else:
	find_clique_multi(args.find_clique_multi)