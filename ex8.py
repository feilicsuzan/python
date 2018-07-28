#number 1
textfile=raw_input("the name of text to read\n");
text=open(textfile);
print "the content of  %s"%textfile;
print text.read();

