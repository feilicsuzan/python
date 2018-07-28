#number 3
'''def circumference(r):
    pi=3.14
    return pi*r*2
from sys import argv;#get three string from terminate
script,c=argv;
if(c=='earth'):
    print"the circumference of earth is",circumference(6078000)
elif(c=='mars'):
    print"the circumference of mars is",circumference(3368000)
else:
    print"please put in correct choose,earth or mars"'''
#how to compare the two float abs(a-b)<1.0e-9
#number 2
a=(1,2,3)
for i in a:
    print i
    print 1+3
b={1:'a',2:'b',3:'c'}
for i in a:#a compared with range(3)
    print b[i]
'''c={1,2,3}#'set' object does not support indexing
for i in range(3):
    print c[i]'''
d={0:'a',1:'b',2:'c'}
for i in range(3):
    print d[i]   
