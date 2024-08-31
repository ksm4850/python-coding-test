# 집위치 x,y
# 한블록 시간 w
# 대각선시간 s 
x,y,w,s = map(int,input().split())

#평행으로만 이동
m1 = (x+y) * w


#대각선으로만 이동
if (x + y) % 2 == 0:# x+y가 짝수면 
    m2 = max(x, y) * s
#대각선이동 + 평행이동 1번
else:# x+y가 홀수면 x,y중 큰값에서 1 빼주고 s값 곱해준 후 w 더하기
    m2 = (max(x, y) - 1) * s + w

#평행이동 + 대각선이동
# x,y중 짧은거리를 대각선으로 이동 후 나머지를 w만큼 이동
m3 = (min(x, y) * s) + (abs(x-y) * w)

# 위 경우의 수 중 가장 작은 값 출력
print(min(m1, m2, m3))


