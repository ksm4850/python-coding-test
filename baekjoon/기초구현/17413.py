S = input()
stack = []

result = ''
chk = False # 괄호 상태 여부
for s in S:
    if s == '<': # 현재 문자가 < 일땐, 스택에 있는 이전 모든 문자들 역순 추가
        chk = True
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(s)
    
    if s == '>': # 문자가 > 일땐, 순차적으로 추가
        chk = False
        for _ in range(len(stack)):
            result += stack.pop(0)

    if s == ' ' and chk == False:
        stack.pop() # 공백제거
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' ' # 공백추가

# 스택에 값이 남아있는경우
if stack:
    for _ in range(len(stack)):
            result += stack.pop()

print(result)

