n = int(input("How many numbers do you want: "))
a=0
b=1
print (a, end=" ")
print (b, end= " ")
for i in range(16):
    c= a+b
    a=b
    b=c
    print(c, end=" ")
