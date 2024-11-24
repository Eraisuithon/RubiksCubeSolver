from collections import deque
import heapq
from Rotations import *

moves = [U, U_, D, D_, L, L_, R, R_, F, F_, B, B_]
SOLVED = f"{'U' * 9}{'F' * 9}{'D' * 9}{'L' * 9}{'R' * 9}{'B' * 9}"


def back(path):
    final = []
    n = SOLVED
    while n in path:
        n, m = path[n]
        final.append(m)
    return final[::-1]


def cost_function(state):
    cost = 0
    for i in range(4, 54, 9):
        if state[i] == state[i - 3]:
            cost -= 1
        if state[i] == state[i + 3]:
            cost -= 1
        if state[i] == state[i - 1]:
            cost -= 1
        if state[i] == state[i + 1]:
            cost -= 1
        if state[i-4] == state[i-3]:
            cost -= 1
        if state[i-3] == state[i-2]:
            cost -= 1
        if state[i+4] == state[i+3]:
            cost -= 1
        if state[i+3] == state[i+2]:
            cost -= 1
        if state[i-4] == state[i-1]:
            cost -= 1
        if state[i+2] == state[i-1]:
            cost -= 1
        if state[i+1] == state[i+4]:
            cost -= 1
        if state[i+1] == state[i-2]:
            cost -= 1
    return cost


def BFS(start):
    path = {}
    vis = {start}
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if cur == SOLVED:
            return back(path)
        for move in moves:
            n = move(cur)
            if n not in vis:
                vis.add(n)
                queue.append(n)
                path[n] = (cur, move.__name__)


def Best_First(start):
    heap = [(cost_function(start), start)]
    vis = {start}
    path = {}
    while heap:
        _, cur = heapq.heappop(heap)
        if cur == SOLVED:
            return back(path)
        for move in moves:
            n = move(cur)
            if n not in vis:
                vis.add(n)
                heapq.heappush(heap, (cost_function(n), n))
                path[n] = (cur, move.__name__)


def A_star(start):
    heap = [(cost_function(start), 0, start)]
    vis = {start}
    path = {}
    while heap:
        _, step, cur = heapq.heappop(heap)
        if cur == SOLVED:
            return back(path)
        for move in moves:
            n = move(cur)
            if n not in vis:
                vis.add(n)
                heapq.heappush(heap, (cost_function(n)+step, step+1, n))
                path[n] = (cur, move.__name__)
