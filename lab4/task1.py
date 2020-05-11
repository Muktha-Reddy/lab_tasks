s=open("alice.txt")
inp = s.readlines()
#print(inp)
def wrd(l):
  #k=[]
  for i in l:
    i.strip("\n")
    for j in i:
      j.strip("")
      
    print(j)
    #print(i)

wrd(inp)
