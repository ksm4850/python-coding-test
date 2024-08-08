"""

등차수열 공식

a1 첫번째 항
an : 마지막항
n : 항의 갯수

(a1 + an) * (n / 2)

MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 2           # 1 ~ 5
        for j <- i + 1 to n - 1   # 2 ~ 6 , 3 ~ 6 , 4 ~ 6 ...
            for k <- j + 1 to n   # 3 ~ 7 , 4 ~ 7, 5 ~ 7  ...
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}

"""

n = int(input())

print(int((n * (n-1) * (n-2)) / 6))
print(3)