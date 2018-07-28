#number 1
'''x=1
y=2
z=3
a='a'
b='b'
c='c'
sets={x,y,z,a,b,c};
diction={'x':x,'y':y,'z':z,4:a,5:b,6:c}
print sets 
print diction
print diction[x]
print sets[1]
diction['extra']=5
print diction'''
#number 2
'''cats=20
dogs=30
if cats<dogs:
    print"More dogs than the cats."
elif dogs<cats:
    print"More cats than dogs."
else:
    print"Same number of cats and dogs."'''
#number 3
def circumference(r):
    pi=3.14
    return pi*r*2
from sys import argv;#get three string from terminate
script,c=argv;
if(c=='earth'):
    print"the circumference of earth is",circumference(6078000)
elif(c=='mars'):
    print"the circumference of mars is",circumference(3368000)
else:
    print"please put in correct choose"
