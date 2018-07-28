x=1
y=2
z=3
a='a'
b='b'
c='c'
test=[x,y,z,a,b,c]
print"x=",x,"y=",y,"z=",z,"a=",a,"b=",b,"c=",c
print test
print "x not in test?",x in test
print "1 in test?",1 in test
print "test+a",test+a
print "test*20",test*20
print  test[2:4]
print len(test)
print min(test)
print"",test.index(2,1,3)
print "",test.count(1)
a={'a':1,2:'b',(1,2):'c'}
print a['a'],a[2],a[(1,2)]
a['extra']=5
print a

