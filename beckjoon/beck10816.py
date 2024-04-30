# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
# 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
import sys

def binarySearch(data, x, start, end):
    if start < end:
        mid = (start + end) // 2
        if data[mid] == x:
            return count.get(x)
        elif data[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
        return binarySearch(data, x, start, end)
    else:
        return 0

N = int(sys.stdin.readline())
sanggeun = sorted(list(map(int, sys.stdin.readline().strip().split())))
M = int(sys.stdin.readline())
M_s = list(map(int, sys.stdin.readline().strip().split()))

count = {}
for card in sanggeun:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for x in M_s:
    print(binarySearch(sanggeun, x, 0, len(sanggeun)-1), end=' ')
