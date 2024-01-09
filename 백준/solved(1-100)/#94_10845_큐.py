import sys
from collections import deque

input = sys.stdin.readline


def save_cmd():
	save = []
	N = int(input())
	for i in range(N):
		line = input().split()
		save.append(line)
	return save


def execute():
	q = deque([])
	cmds = save_cmd()
	for cmd in cmds:
		if cmd[0] == "push":
			q.append(cmd[1])
		elif cmd[0] == "pop":
			if q: print(q.popleft())
			else: print(-1)
		elif cmd[0] == "size":
			print(len(q))
		elif cmd[0] == "empty":
			if q: print(0)
			else: print(1)
		elif cmd[0] == "front":
			if q: print(q[0])
			else: print(-1)
		elif cmd[0] == "back":
			if q: print(q[-1])
			else: print(-1)
		else:
			print("not case")

execute()

# 20 min