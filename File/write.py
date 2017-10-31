hand=open("write.txt",'w')
hand.write("Coding in python.\n")
hand.write("I love python.\n")
hand.close()
hand=open("write.txt",'r')
for i in hand:
  print(i)