"""

"""


while True:
    n = int(input())

    if n == -1:
        break

    num_list = []
    for i in range(1, n//2+1):
        if n%i == 0:
            num_list.append(i)

    if n == sum(num_list):
        print(f"{n} = {' + '.join(str(num) for num in num_list)}")
    else:
        print(f"{n} is NOT perfect.")

