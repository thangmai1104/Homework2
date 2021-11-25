a=[]
n=input("n=")
for j in range(n):
    a[j]=input("a[i]=")
max=a[0]
for i in range(n) :
    if a[i]>max:
        max=a[i]
print(max)