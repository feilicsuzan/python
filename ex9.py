#number 1
'''textfile=raw_input("please put in the textfile to be copied\n");
text=open(textfile);
s=text.read();
text.close();
text1=open("mytext1.txt",'w+');
text1.write(s);
text1.seek(0);#put the stream at beginning
print text1.read();
text1.close();'''
#number 2
'''def print_none():
    print "hello world"*20
def print_one(arg):
    print "i like %r"%arg
def print_two(arg1,arg2):
    print "i like %r and %r"%(arg1,arg2)
print_none()
print_one("ban")
print_two("ban","apple")'''
#number 3
def add(a,b):
    return a+b
groupa=20
groupb=30
total=add(groupa,groupb)
print"total is %d"%total
