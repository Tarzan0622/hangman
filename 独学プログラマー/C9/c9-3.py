import csv

lists=[["Top Gun", "Risky Business", "Minority report"], ["Titanic","The revenant","Inception"],["Training Day", "Man on Fire", "Flight"]]

with open("list.csv","w") as f:
  w=csv.writer(f,delimiter=",")
  for movie_list in lists:
    w.writerow(movie_list)