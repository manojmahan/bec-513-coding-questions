import sys
import pandas as pd
# zcat data/q1_data.tsv.gz | awk 'NR==1||/ENSG/'  | python question1.py data/to_select.tsv  > outputs/q1.tsv
toselect = list(pd.read_csv(sys.argv[1],sep='\t',names=['query'])['query'])
#print(toselect)
header = False
for line in sys.stdin:
    if not header:
        header=line
        print(line,end='')
        continue
    for q in toselect:
        if  q in line:
            print(line,end='')
