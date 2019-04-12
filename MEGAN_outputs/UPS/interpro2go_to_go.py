import urllib.request
import re

response = urllib.request.urlopen('http://current.geneontology.org/ontology/external2go/interpro2go')


i2go = 'IPR001782 Flagellar P-ring protein'

def interpro2GO(i2go):
    go_regex = re.compile('GO:\d+')
    GO_terms = [];
    for line in response.read().decode('utf-8').split('\n'):
        if i2go in line:
            GO_terms.append(go_regex.search(line)[0])
    return GO_terms


print(interpro2GO(i2go))
