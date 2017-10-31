d=dict()
s="Hi i am making a program for dictionary and i hope you will like it"
for i in s:
    d[i]=d.get(i,0)+1
print(d)