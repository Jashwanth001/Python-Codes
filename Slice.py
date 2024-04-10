str1 = input("Enter a name:")
n = input("Choose a index to remove:")
str2 = str1[:n]
str3 = str1[n+1:]
str4 = str2 + str3
print("Final",str4)