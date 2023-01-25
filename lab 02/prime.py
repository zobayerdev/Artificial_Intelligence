count = 0
i = 2
flag = 0
while count <= 50:
     flag = 0
     x = int(i / 2)
     for j in range (2, x):
         if i % j == 0:
             flag = 1
             break
     if flag == 0:
         print(i)
         count = count + 1
     i = i + 1