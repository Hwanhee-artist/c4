print("Welcome to Hwanhee's Connect 4!")
print("")

print(" 1 2 3 4 5 6 7")
for i in range(6):
  print("| | | | | | | |")

c = "| | | | | | | |"
c1 = "| | | | | | | |"
c2 = "| | | | | | | |"
c3 = "| | | | | | | |"
c4 = "| | | | | | | |"
c5 = "| | | | | | | |"
c6 = "| | | | | | | |"
c7 = "| | | | | | | |"
row = "- - - - - - -"
one = "player 1's move:"
two = "player 2's move:"
numbers = (" 1 2 3 4 5 6 7 ")

def replace(list, X, Y):
   while X in list:
      bo = c1[X]
      list. remove(bo)
      list. insert(X,Y)

move = input()
if move == "1":
  print (one)
  print(" 1 2 3 4 5 6 7")
  for i in range(5):
    print (c)
  replace(c1,1,"O")
  print(c1)

if move == "2":
  print(one)
  print(" 1 2 3 4 5 6 7")
  for i in range(5):
    print (column)
  print ("| |O| | | | | |")

if move == "3":
  print (one)
  print(" 1 2 3 4 5 6 7")
  for i in range(5):
    print (column)
  print ("| | |O| | | | |")

if move == "4":
  print(one)
  print(" 1 2 3 4 5 6 7")
  for i in range(5):
    print (column)
  print ("| | | |O| | | |")

if move == "5":
  print(one)
  print(" 1 2 3 4 5 6 7")
  for i in range(5):
    print(column)
  print("| | | | |O| | |")

if move == "6":
  print(one)
  print(" 1 2 3 4 5 6 7")
  for i in range(5):
    print(column)
  print("| | | | | |O| |")

if move == "7":
  print(one)
  print(" 1 2 3 4 5 6 7")
  for i in range(5):
    print(column)
  print("| | | | | | |O|")

