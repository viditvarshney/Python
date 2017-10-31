fhand=open("world")
d=dict()
for line in fhand:
    word=line.split()
    for i in word:
         if i not in d:
            d[i]=1
         else:
            d[i]=d[i]+1
print(d)
