import os


if os.path.exists("token.txt"):
  os.remove("token.txt")
else:
  print(".creating file token.txt")


token = open('token.txt', 'a')
token1 = input('Enter Your token: ')
token.write(token1)
token.close()




print("Your token: "+ token1)

