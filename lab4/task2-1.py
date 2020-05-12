#import string
new=open("alice.txt")
words=new.readlines()
def count(ip):
  cnt=0
  for i in ip:
    nl=i.split(" ")
    for j in nl:
      b=j.strip("\n")
      cnt=cnt + 1
  print("number of words:",cnt)
count(words)
