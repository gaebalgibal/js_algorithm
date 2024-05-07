import sys
# input()는 반복문으로 여러줄을 입력 받아야 할때 오래 걸리니 sys.stdin.readline()를 사용하자

class Queue:
    def __init__(self):
        self._queue = []

    def push(self, x):
        self._queue.append(x)
    
    def pop(self):
        if len(self._queue) == 0:
            print(-1)
        else:
            print(self._queue.pop(0))
    
    def size(self):
        print(len(self._queue))
    
    def empty(self):
        print(1) if (len(self._queue) == 0) else print(0)

    def front(self):
        if len(self._queue) == 0:
            print(-1)
        else:
            print(self._queue[0])
    
    def back(self):
        if len(self._queue) == 0:
            print(-1)
        else:
            print(self._queue[-1])

N = int(sys.stdin.readline())
queue = Queue()

for i in range(N):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        queue.push(order[1])
    if order[0] == 'pop':
        queue.pop()
    if order[0] == 'size':
        queue.size()
    if order[0] == 'empty':
        queue.empty()
    if order[0] == 'front':
        queue.front()
    if order[0] == 'back':
        queue.back()
    