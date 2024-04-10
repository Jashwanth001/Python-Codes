"""
n = int(input("Enter a Number:"))
if(n%2!=0):
    print("Weird")
elif(n%2==0):{
    print("Not Weird")
}
elif(n%2==0 and n in range(2,5)):
    print("Not Weird")
elif(n%2==0 and n in range(6,20)):
    print("Weird")
else:
    print("Not")

N = int(input("N in his pocket:"))
C = int(input("The price of the chocolate:"))
M = int(input("Wrappers:"))
buy = N*C
m = M+1
print((buy))

x =10
while x:
    x = x-1
    if x%2!=0:
        print(x,end='')
"""
i = int(input("number:"))
print("Num is",format(i,"0.2f"))

