#number 1
#textfile=raw_input("the name of text to read\n");
#text=open(textfile);
#print "the content of  %s"%textfile;
#print text.read();
#number 2
textfile=raw_input("the name of text to write\n");
text=open(textfile,'a');#you could replace a with w(from the beginning),r(
line1="i am good at ";
line2="if you listened my ";
line3="you will ";
text.write(line1);
text.write("\n");
text.write(line2);
text.write("\n");
text.write(line3);
text.write("\n");
text.close();
