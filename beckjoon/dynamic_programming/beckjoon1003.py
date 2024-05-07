# 시간 초과
'''
def fibo(i):
    if i == 0:
        cache[0] += 1
        return 0
    elif i == 1:
        cache[1] += 1
        return 1
    else:
        return fibo(i - 1) + fibo(i - 2)

T = int(input())

for _ in range(T):
    cache = [0, 0]
    N = int(input())
    fibo(N)
    print(cache[0], cache[1])
'''

T = int(input())

D = [[]] * 41

D[0] = [1, 0]
D[1] = [0, 1]
D[2] = [1, 1]

for _ in range(T):
    N = int(input())

    for i in range(3, N+1):
        D[i] = [D[i - 1][0] + D[i - 2][0],D[i - 1][1] + D[i - 2][1]]
    print(D[N][0], D[N][1])