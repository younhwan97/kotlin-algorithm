import sys
from queue import PriorityQueue

N = int(input())

pq = PriorityQueue()

for _ in range(N):
    value = int(sys.stdin.readline())

    if value == 0:
        if pq.qsize() == 0:
            print(0)
        else:
            print(-1 * pq.get())
    else:
        pq.put(-1 * value)