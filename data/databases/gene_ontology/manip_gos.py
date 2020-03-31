from goatools import obo_parser
from goatools import mapslim
import sys

go = obo_parser.GODag('GO_files/go-basic.obo')
goslim = obo_parser.GODag('GO_files/go-slim.obo')

def set_of_all_ancestors(terms):
    all_ancestors = set(terms)
    for i in set(terms):
        if i in go.keys():
            all_ancestors.update(go[i].get_all_parents())
    return all_ancestors

def get_all_ancestors(infile, outfile):
    f = open(infile, 'r')
    gos = [x.strip() for x in f.readlines()]
    f.close()
    
    gos_with_ancestors = set_of_all_ancestors(gos)
    
    with open(outfile, 'w') as outf:
        for x in gos_with_ancestors:
            outf.write(x + '\n')

def slim_down(infile, outfile):
    f = open(infile, 'r')
    gos = [x.strip() for x in f.readlines()]
    f.close()
    
    slims = set()
    for i in gos:
		if i in go.keys():
			slims.update(mapslim.mapslim(i, go, goslim)[1])
		else:
			print(i + " not found")
    
    with open(outfile, 'w') as outf:
        for x in slims:
            outf.write(x + '\n')
            
for i in ['eggnog', 'megan', 'metagomics', 'unipept', 'mpa']:
	infile = 'go_lists/' + i + '.tab'
	outfile = 'go_lists/' + i + '_parents.tab'
	outslim = 'go_lists/' + i + '_slim.tab'
    # get_all_ancestors(infile, outfile)
	print i
	slim_down(infile, outslim)

        
