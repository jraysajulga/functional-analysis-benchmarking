import urllib.request
import re
import xlrd

response = urllib.request.urlopen('http://current.geneontology.org/ontology/external2go/interpro2go')

def interpro2GO(i2go):
    response = urllib.request.urlopen('http://current.geneontology.org/ontology/external2go/interpro2go')
    go_regex = re.compile('GO:\d+')
    GO_terms = [];
    for line in response.read().decode('utf-8').split('\n'):
        if i2go in line:
            GO_terms.append(go_regex.search(line)[0])
    return GO_terms

#print(f.readline())
#interpro2GO(interpro2GO_map, term)

workbook = xlrd.open_workbook('UPS1_03_reads to IP2G.xlsx', 'UPS1_03-ex.txt')
worksheet = workbook.sheet_by_index(0)

print(interpro2GO('IPR001782 Flagellar P-ring protein'))
test = worksheet.cell_value(0,1).replace('"','').strip()
print(test)
print(interpro2GO(test))

#for row in range(worksheet.nrows):
    #print(interpro2GO(worksheet.cell_value(row, 1).replace('"','').strip()))

#    interpro2GO(worksheet.cell_value(row, 1))
    #print(interpro2GO(worksheet.cell_value(row, 1)))
