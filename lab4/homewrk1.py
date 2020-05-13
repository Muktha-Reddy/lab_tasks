s=open("words.txt")
wl=s.readlines()
t=open("alice.txt")
f2=t.readlines()
wrds=[]
for i in wl:
  a=i.split()
  for j in a:
    j.strip("\n")
    #print(j)
    wrds.append(j)
#print(wrds)
#print(fl) 
wrdlist=set(wrds)
bookwords=set(fl)
f3=bookwords.difference(wrdlist)
print(list(f3))
