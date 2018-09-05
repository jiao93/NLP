import sys

f = open('hightemp.txt')
for i in range(int(sys.argv[1])):
    print(f.readline(),end='')