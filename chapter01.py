#coding=utf-8
from functools import reduce
from random import sample

def solution_00(s='stressed'):
    return s[::-1]

def solution_01():
    return 'パタトクカシーー'[::2]

def solution_02():
    a = 'パトカー'
    b = 'タクシー'
    z = zip(a,b)
    return reduce(lambda x,y:''.join(x)+''.join(y),z)

def solution_03():
    s = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    words = s.replace(',','').replace('.','').split()
    return [len(i) for i in words]

def solution_04():
    s = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    words = s.replace('.','').split()
    a = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    # assume that index starts from 1
    words = [words[i][0:2-(i+1 in a)] for i in range(len(words))]
    d = dict([(words[i],i+1) for i in range(len(words))])
    return d


bi_gram = lambda x:[(x[i],x[i+1]) for i in range(len(x)-1)]
#used in 05 and 06

def solution_05():
    s = 'I am an NLPer'
    word_bi_gram =  bi_gram(s.split())
    char_bi_gram = bi_gram(s)
    return (word_bi_gram,char_bi_gram)

def solution_06():
    a = 'paraparaparadise'
    b = 'paragraph'
    x = set(bi_gram(a))
    y = set(bi_gram(b))
    se = tuple('se')
    return (x & y,x | y,x-y,y-x,se in x,se in y)

render = lambda x,y,z:'{}時の{}は{}'.format(x,y,z)
#used in 07

def solution_07():
    return render(12,'気温',22.4)

def solution_08(s):
    return ''.join(chr(219-ord(i)) if i.islower() else i for i in s)

def solution_09():
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = s.split()
    shuffle = lambda s:s[0]+''.join(sample(s[1:-1],len(s)-2))+s[-1]
    return ' '.join(''.join(shuffle(i)) if len(i)>4 else i for i in words )

if __name__ == '__main__':
    print(solution_00())
    print(solution_01())
    print(solution_02())
    print(solution_03())
    print(solution_04())
    print(solution_05())
    print(solution_06())
    print(solution_07())
    print(solution_08('Hello World'),solution_08((solution_08('Hello World'))))
    print(solution_09())
