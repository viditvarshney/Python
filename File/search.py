word=input("Enter the word you want to search for")
hand=open("kaus.txt")
for i in hand:
    if i.startswith(word):
        print(i)