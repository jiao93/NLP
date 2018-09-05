import csv
from collections import defaultdict

def solution_17():
    s = set()
    with open('hightemp.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            s.add(row[0])
    return s

def solution_18():
    l = []
    with open('hightemp.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            l.append(row)
    return ['\t'.join(i) for i in sorted(l,key=lambda x:x[2],reverse=True)]

def solution_19():
    d = defaultdict(lambda :0)
    with open('hightemp.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            d[row[0]]+=1
    return [i[0] for i in sorted(d.items(),key=lambda x:x[1],reverse=True)]

if __name__ == '__main__':
    print(solution_17())
    print('\n'.join(solution_18()))
    print(solution_19())