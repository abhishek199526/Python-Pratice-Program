# name= input("महोदय आपका शुभ नाम ?  ")
# for index in name :
#     print(index)

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print("आपका दिन शुभ हो 👍😎👌🎈")
# print("स्वाथ्य रहें मस्त रहें 👓🎃🎃😊")
# word="I am fine"
# n=len(word)
# word1=word.upper()
# word2=word.lower()
# converted_word=""
# for i in range(n):
#     if i%2==0:
#         converted_word+= word2[i]
#     else :
#         converted_word+= word1[i]  
# print(converted_word)

# x="Kacha badam"
# for i in range(len(x)-1,-1,-1):
#     print(i)
#     print(x[i])

# name=input("What is your  name: ")
# age=input("How old are you:")
# year=str((2022-age)+100)
# print("")
n=int(input("Enter Number"))
sum=0
for num in range(1,n+1,1):
    sum+=num
print("Sum of fisrt ",n,"numbers is :",sum)
avg=sum/n
print("Avg = ",n, "num = ",avg)
n=5
k=5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()
    
