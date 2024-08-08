import sys
input=sys.stdin.readline
def sol():
    n,m,b=map(int,input().split())
    data=[0]*257 # 블록 최대높이만큼 배열선언

    # 블록높이 갯수 초기화
    for _ in range(n):
        for i in map(int,input().split()):
            data[i]+=1
    # 현재 블록들의 높이 합( 갯수 * 높이)
    have=sum(i*data[i] for i in range(257))
    # 초기 최소 시간 설정
    # 모든 블록을 제거하는 경우를 고려해서 초기값 설정
    ans=(have*2,0)
    need=0 # 블록 추가시 필요한 블록 수
    t=data[0] # 초기 높이 0의 블록 갯수
    nm=n*m # 전체 블록의 개수

    for i in range(1,257): # 높이만큼 반복
        need+=t # 현재 높이로 맞추기 위해 필요한 블록 수 증가
        have-=nm-t # 현재 높이에서 블록 제거
        t+=data[i] # 다음 높이의 블록 개수 추가
        if have+b-need<0: # 추가블록 부족하면 루프 종료
            break
        else:
            ans=min((have*2+need,-i),ans) # 현재 높이에서 최소 시간 계산하여 갱신
    print(ans[0],-ans[1])
sol()