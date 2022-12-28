# f= open("My_First_file.txt","w")
# # x="जय जिन्नेंद्र"
# x="Jai Jinnedra\n"
# f.write(x)
# y="Jai Mahaveer"
# f.write(y)

# f.close()
f= open("My_First_file.txt","r")
x=f.read()
print(x)
f.close()
