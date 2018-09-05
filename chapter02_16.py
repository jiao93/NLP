import sys

f = open('hightemp.txt')
lines = f.readlines()
n = int(sys.argv[1])
each = len(lines)//n
if len(lines)-(n-1)*each>n-1:
    each+=1
for i in range(n-1):
    for j in range(each):
        print(lines[i*each+j][:-1])
    print()

for j in range((n-1)*each,len(lines)):
    print(lines[j][:-1])

