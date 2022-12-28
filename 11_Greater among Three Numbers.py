

a = int(input("भाईसाहब! पहला नंबर दो :"))
b = int(input("भाईसाहब! दूसरा नंबर दो :"))
c = int(input("भाईसाहब! तीसरा नंबर दो :"))
if a == b and b == c and a == c:
    print("All values are same")

elif a == b and c < a:
    print(a, " and ", b, " is greater than ", c)

elif b == c and a < b:
    print(b, " and ", c, " is greater than ", a)
elif a == c and b < a:
    print(a, " and ", c, "is greater than ", b)

elif a > b and a > c:
    print(a, "is greater than", b, "and ", c)
elif b > a and b > c:
    print(b, "is greater than", a, "and ", c)


else:
    print(c, "is greater than", a, "and ", b)

print("धन्यवाद भाईसाहब")


# Write a python script for  finding greatest among N user numbers
# To get best of 2 marks from excel sheet.
