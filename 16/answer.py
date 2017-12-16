#!/usr/bin/env python3
# encoding: utf-8

from collections import deque
import sys

# https://www.reddit.com/r/adventofcode/comments/7k572l/2017_day_16_solutions/drbp1ex/
def dance(instructions, iterations):
	instructions = instructions.split(',')
	que = deque('abcdefghijklmnop')
	for i in range(iterations):
		for instr in instructions:
			if instr.startswith('s'):
				rot = int(instr[1:])
				que.rotate(rot)
			elif instr.startswith('x'):
				a, b = map(int, instr[1:].split('/'))
				que[a], que[b] = que[b], que[a]
			elif instr.startswith('p'):
				x, y = instr[1:].split('/')
				a = que.index(x)
				b = que.index(y)
				que[a], que[b] = que[b], que[a]
		if que == deque('abcdefghijklmnop'):
			return i+1
	return ''.join(que)

instructions = sys.stdin.read().strip()
print(dance(instructions, 1))
cycle = dance(instructions, 10**9)
enough = 10**9 % cycle
print(dance(instructions, enough))