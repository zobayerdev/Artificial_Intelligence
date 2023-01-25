year = eval(input("Enter year: "))

x = year % 4

if x == 0:
   print("leap year",year);
else:
   print("not leap year", year);