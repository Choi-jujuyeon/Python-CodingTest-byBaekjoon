a=[1, 2, 3, 4, 3, 2, 1]
print(a)
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)
