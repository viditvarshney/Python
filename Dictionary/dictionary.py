d=dict()
s="Hi i am making a program for dictionary and i hope you will like it"
l=list()
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)