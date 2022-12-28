# Write a python script to write the execution time for a variable in a fole where the variable is used to find file where the variable is used to find factorial using iterative & recursion method
import time

def fact_iterative(n):
    facto=1
    if(n==0):
        # print("Factorial of 0 is 1")
        return 1
    else:
        for i in range(1,n+1):
            facto=facto*i
        return facto
        # print("Factorial of ",n," is :",facto )
        
def fact_recursive(n):
    
    if(n==0):
        # print("Factorial of 0 is 1")
        return 1
    else:
         
        return n*fact_recursive(n-1)
        # print("Factorial of ",n," is :",facto )
# Time Calculation for Iterative method 
start_iter =time.time()
for i in range(5,1000,5):
    fact_iterative(i)
end_iter =time.time()
exe_iter=end_iter-start_iter
f=open("15_Python_Script","w")
exe_iterative=str(exe_iter)
f.write("Execution time of Iterative Method is "+exe_iterative)


# Excution time calulation for Recursive method 
start_recursive=time.time()
for i in range(5,1000,5):
    fact_recursive(i)
end_recusive =time.time()
exe_recursive=end_recusive-start_recursive
exe_recur=str(exe_recursive)
f.write("\nExecution time of Recursive Method is "+exe_recur+"\n")

# exe_diff=exe_recursive-exe_iter
# exe_difference=str(exe_diff)
# f.write("Difference between Recursive amd Iterative method is : " + exe_diff)


f.close()
