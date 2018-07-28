#number 1 child and parents has the same function
'''class parent(object):
    def implicit(self):
        print"parent implict()"
class child(parent):
    def __init__(self):
        super(parent,self).__init__()
#please put in the below in python of catalogue repo/python'''
'''import cla_com as c
dad=c.parent()
son=c.child()
dad.implicit()
son.implicit()'''
#number 2 child and parent has the differnt function
'''class parent(object):
    def override(self):
        print"parent override()"
class child(parent):
    def __init__(self):
        super(parent,self).__init__()
    def override(self):
        print"child override()"      '''
#please put in the below in python of catalogue repo/python
'''import cla_com as c
dad=c.parent()
son=c.child()
dad.override()
son.override()'''#if there is something wrong,please quit python,then have a try
#number 3
'''class parent(object):
    def altered(self):
        print"parent altered()"
class child(parent):
    def __init__(self):
        super(parent,self).__init__()
    def altered(self):
        print"child altered()" 
        super(child,self).altered() '''#there will be"parent altered()"
#please put in the below in python of catalogue repo/python
'''import cla_com as c
dad=c.parent()
son=c.child()
dad.altered()
son.altered()'''
#number 4 multiple inheritance
class child(object):
    def para(self):
        print"child likes sing"
class male(object):
    def chara(self):
        print"male is strong"
class boy(child,male):
    def __init__(self):
        child.__init__(self)
        male.__init__(self)
#please put in the below in python of catalogue repo/python
'''import cla_com as c
chi=c.child()
ma=c.male()
bo=c.boy()
bo.para()
bo.chara()'''      
#number 5 the composition of two class
'''class parent(object):
    def fun(self):
        print"parent fun()"
class child(object):
    def __init__(self):
        self.parent=parent()
    def fun(self):
        self.parent.fun()'''
#please put in the below in python of catalogue repo/python
'''import cla_com as c
dad=c.parent()
son=c.child()
dad.fun()
son.fun()'''      
