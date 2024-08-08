"""
함수의 시간복잡도 구하기

수행횟수와 최고차항(다항식 안에서 차수가 가장 높은 항) 차수 출력


MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}

(n + n + ... + n) - (1 + 2 + ... + 6)

n을 n-1번 더한 수에 첫째항이 1이고 마지막항이 n-1인 등차수열의 합을 빼주면됨


등차수열 공식

a1 첫번째 항
an : 마지막항
n : 항의 갯수

(a1 + an) * (n / 2)
"""

n = int(input())
print(int(n*(n-1)-(n-1)*n/2))
print(2)
