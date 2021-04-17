#### for 문
value = int(input("정수 입력:"))
cnt = 0 # 짝수의 개수를 저장할 변수
for i in range(value, 0, -1):
    if i % 2 != 0:
        continue
    print(i)
    cnt = cnt + 1 # 홀수일때는 위의 if 문 때문에 어쩌피 이 문장을 안 실행해서
                  # 짝수일떄만 cnt 가 1 씩 늘어나!

print("----------")
print(cnt, "개")

#### while 문
value = int(input("정수 입력:"))
cnt = 0 
while (value > 0):  # value 부터 1 까지는 while문 이하를 실행하고 0이 되면 자동으로 
                    # while문을 빠져나와!
    if value % 2 == 0: # 짝수일때! 로 조건 바꿔봤엉
        print(value)
        cnt = cnt + 1 
    value  = value - 1 # while 문을 한번씩 돌때마다 value를 -1씩 해줘서 6 다음 5, 
                       # 5 다음 4 를 검사하게 해줘

print("----------")
print(cnt, "개")
