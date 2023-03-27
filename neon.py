a=int(input('enter the number: '))
b=a**2
c=str(b)
print(c)
i=0
d=0
while i<len(c):
    d+=int(c[i])
    i+=1
if d==a:
    print('it is neon')
else:
    print('it is not neon')
