li = [10,20,30];
print(li);

li.append(40);
print(li);

li.remove(10);
print(li)

for el in li:
    print(el);

for i in range(len(li)):
  print(i, li[i]);

for i, v in enumerate([20,30,40]):
  print(i, v);