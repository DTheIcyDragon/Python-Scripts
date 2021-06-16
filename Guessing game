import random
import time

wcounter = 0
lcounter = 0 

while True:
  rand1 = random.randint(0,23)
  rand2 = random.randint(33,57)

  randzahl = random.randint(rand1, rand2)

  print("Wins: " + str(wcounter))
  print("Loses: " + str(lcounter))
  userin = input('Bitte gib eine Zahl zwischen ' + str(rand1) + ' und ' + str(rand2) + ' ein.\n')

  if int(userin) == int(randzahl):
    print('Richtig\n')
    time.sleep(5)
    wcounter = wcounter + 1

  else:
    print('Falsch, richtig war: ' + str(randzahl) + '\n')
    time.sleep(5)
    lcounter = lcounter + 1
