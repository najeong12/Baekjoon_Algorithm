ll = [1, 4, 7]
rr = [3, 6, 9]

def solution(numbers, hand):
    answer = ''
    left = 10
    right = 12
    for num in numbers:
        if num == 0:
            num = 11
        if num in ll:
            answer += 'L'
            left = num
        elif num in rr:
            answer += 'R'
            right = num
        else:
            if (abs(num - left)//3 + abs(num - left) % 3) < (abs(num - right)//3 + abs(num - right) % 3):
                answer += 'L'
                left = num
            elif (abs(num - left)//3 + abs(num - left) % 3) > (abs(num - right)//3 + abs(num - right) % 3):
                answer += 'R'
                right = num
            else:
                if hand == "right":
                    answer += 'R'
                    right = num
                else:
                    answer += 'L'
                    left = num
            
    return answer
