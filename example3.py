num = int (input("Enter any Integer"))
sum = 0
while num > 0:
    sum = sum * 10  + (num % 10)
    num =int( num / 10)

print(sum)