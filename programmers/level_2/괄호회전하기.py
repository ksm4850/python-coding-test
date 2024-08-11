def solution(s):
    answer = 0
    s = list(s)
    for _ in range(len(s)):
        stack = [] # 스택초기화
        for i in range(len(s)):
            if len(stack) > 0: # 스택이 비어있지 않다면
                # 마지막에 들어온 값과 비교 후 괄호 문자열이면 스택 pop
                if stack[-1] == '[' and s[i] == ']': stack.pop()
                elif stack[-1] == '{' and s[i] == '}': stack.pop()
                elif stack[-1] == '(' and s[i] == ')': stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i]) 
        if len(stack) == 0: # 스택이 비어있다면 올바른 괄호 문자열
            answer += 1
        s.append(s.pop(0)) # 배열 회전
        
    return answer