import string
s=open("alice.txt",'r')
inp = s.readlines()
#print(inp)
def wrd():
  for i in inp:
     nl = i.split(' ')
     #print(nl)
     for j in nl:
       b=j.strip("\n")
       for k in b:
         if k in string.punctuation:
           b = b.replace(k,"")
       b=b.lower()
       print(b)
wrd()
