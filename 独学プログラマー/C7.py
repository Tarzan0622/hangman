1,3
movies=["ウォーキング・デッド", "アントラージュ", "ヴァンパイア・ダイアリーズ"]
for index, movie in enumerate(movies):
  print(index)
  print(movie)

2
for i in range(25,51):
  print(i)

4
numbers=[11,32,33,15,1]
while True:
  answer=input("write a number or q to quit")
  if answer =="q":
    break
  try:
    answer =int(answer)
  except ValueError:
    print("please write a number or q to quit")
  if answer in numbers:
    print("correct!")
  else:
    print("incorrect!")

5
list1=[8,19,148,4]
list2=[9,1,33,83]
times=[]
for i in list1:
  for j in list2:
    times.append(i*j)
print(times)
