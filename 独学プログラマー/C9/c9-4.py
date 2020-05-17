import csv

lists=[["トップガン", "リスキービジネス", "マイノリティーレポート"], ["タイタニック","反逆者","無罪"],["訓練の日", "燃える男", "フライト"]]

with open("lista.csv","w", encoding="cp932") as f:
  w=csv.writer(f,delimiter=",")
  for movie_list in lists:
    w.writerow(movie_list)