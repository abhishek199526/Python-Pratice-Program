n= int(input("Enter Number :"))
is_prime = True
for i in range(2,n):
    if n%i==0:
        is_prime=False
        break
if is_prime:
    print("Prime Number")
else :
    print("Not a Prime Number")

