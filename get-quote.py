import random
# import time

# last = len(quotes) - 1
# rnd = random.randint(0, last)

def important():
 #print("Keep it logically awesome.")

  f = open("D:\D-Prasanna\Tutorial Docs\python\python101\python-random-quote\quotes.txt")
  quotes = f.readlines()
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  f.close()

  print(quotes[rnd])
if __name__== "__main__":
  #while True:
   important()
   #time.sleep(5)
