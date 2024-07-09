n=input("enter the word:")
l=d=0
for i in n:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        pass

print("letter:",l)
print("digit:",d)
        
