import sys

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0
for i in range(N+1):
    result += sum(arr[0:i])

print(result)