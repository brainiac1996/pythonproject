import math
def func(x):
    a = x ** 2
    return a
def sgn(x):
    """
    python
    """
    if x > 0:
        a = +1
    elif x < 0:
        a = -1
    else:
        a = 0
    return a
#print(sgn(2.1))
#print(sgn(0))
#print(sgn(-2))
#print(help (sgn))
#c=1/7
#print(math.ceil(c))
#print(math.floor(c))
#print(math.pow(2,3))
#"""
#list
#"""
#l=[1,2,3]
#print(type(l))
#l[0]=5
#print(l)
#"""
#tuple
#"""
#b=(1,2,3)
#
#print(b[0])

#l1=list(range(5))
#print(type(l1))
#print(l1)
#
#for k in l1:
#    print(k**2)
#
#for i in [10,20]:
#    for j in ["ab","ac"]:
#        print(i,j)
#
#x1=(0,1,2,3,4)
#print(x1[1:4])
#
#def primes(N):
#    sieve=set(range(2,N))
#    for i in range(2,round(math.sqrt(N))):
#        if i in sieve:
#            sieve-=set(range(2*i,N,i))
#    return sieve
#
#print(primes(20))

#%lsmagic
#%whos

#x,y =True,False
#print(x and y)
#print(x or y)
#print(not y)
#print(x and y)
#print((1==2)|(2==2))
# найти в строке вещественное число
#str="bdsjbfjsfb5.6dfjsihs"

#s=[1,'string',[1,2,3],True]
#print(s[1][1])
person = ["Ivan", "Ivanov",22,"may",2001]
NAME, BIRTHDAY = slice(3),slice(3,None)
print(person[NAME],person[BIRTHDAY])
max(person)