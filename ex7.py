#number 1
from sys import argv;#get three string from terminate
script,r=argv;
r=float(r);
pi=3.14;
print "the circumferences of earth",(r*2*pi);
#number 2
from sys import argv;
script,textfile=argv;
text=open(textfile);
print "the content of  %s"%textfile;
print text.read();
