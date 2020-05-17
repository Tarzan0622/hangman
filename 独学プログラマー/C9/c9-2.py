import csv
answer=input("what is your fav color?")

with open("questionanswer.csv","w", newline='') as f:
  f.write(answer)
