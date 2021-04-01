N = int(input())
arr=[]
result=[]
temp=[]

for _ in range(N):
    arr.append(int(input()))

j = 0
for i in range(1, N+1):
    temp.append(i)
    result.append('+')
    while (temp and temp[-1] == arr[j]):
        temp.pop()
        j += 1
        result.append('-')

if not temp: # 비어 있으면
    for i in result:
        print(i)
else:
    print("NO")