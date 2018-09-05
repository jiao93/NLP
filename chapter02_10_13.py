import csv
def solution_10():
    f = open('hightemp.txt')
    l = len(f.readlines())
    f.close()
    return l

def solution_11():
    f = open('hightemp.txt')
    f2 = open('hightemp_11.txt','w')
    lines = f.readlines()
    f2.writelines([i.replace('\t',' ') for i in lines])
    f.close()
    f2.close()

def solution_12():
    f1 = open('col1.txt','w')
    f2 = open('col2.txt','w')
    with open('hightemp.txt') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for row in reader:
            print(row[0],file=f1)
            print(row[1],file=f2)
    f1.close()
    f2.close()

def solution_13():
    f1 = open('col1.txt','w')
    f2 = open('col2.txt','w')
    f3 = open('hightemp_13.txt','w')
    lines_1 = f1.readlines()
    lines_2 = f2.readlines()
    assert(len(lines_1)==len(lines_2))
    for i in range(len(lines_1)):
        print(lines_1[i],lines_2[i],sep='\t',file=f3)
    f1.close()
    f2.close()
    f3.close()

if __name__ == '__main__':
    print(solution_10())
    solution_11()
    solution_12()