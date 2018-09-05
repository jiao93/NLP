import sys

f = open('hightemp.txt')
lines = f.readlines()
f.close()
print(''.join(lines[-int(sys.argv[1]):]))
#not efficient because non-accessary lines are read
#can be improved using seek, but it is more compex