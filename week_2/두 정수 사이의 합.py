# 두 정수 사이의 합
def soulution(a, b):
    answer = 0
    
    if a == b:
        answer = a
        
    else:
        if a < b:
            for i in range(a, b+1):
                answer += i
        elif a > b:
            for i in range(b, a+1):
                answer += i
                
    return answer
print(soulution(5, 1))