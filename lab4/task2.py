from collections import Counter
new=open("alice.txt")
words=new.readlines()
def count(ip):
  cnt=0
  fl=[]
  d={}
  for i in ip:
    nl=i.split(" ")
    for j in nl:
      b=j.strip("\n")
      fl.append(b)
      cnt=cnt + 1
  for k in fl:
    if k not in d:
      d[k]=1
    else:
      d[k] +=1
  ct=Counter(d)
  first_twenty=ct.most_common(20)
  #print(first_twenty)
  print("number of words:",cnt)
  print("Most 20 frequently used words are :")
  for ft in first_twenty:
    print(ft[0], end =" ")
  print("Number of different words:")
  dfwrds=len(set(d))
  print(dfwrds)
count(words)
