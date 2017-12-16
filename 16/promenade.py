#!/usr/bin/env python3
# encoding: utf-8

from collections import deque
from string import ascii_lowercase
import sys

from ben import input_iter


def dance(moves, size=16, iterations=1):
	moves = moves.split(',')
	progs = deque(ascii_lowercase[:size])

	for i in range(iterations):
		for move in moves:
			if move[0] == 's':
				progs = spin(progs, int(move[1:]))
			if move[0] == 'x':
				progs = exchange(progs, *map(int, move[1:].split('/')))
			if move[0] == 'p':
				progs = partner(progs, *move[1:].split('/'))
		if moves == ascii_lowercase[:size]:
			return i+1

	return ''.join(progs)


def part2(moves, size=16):
	cycle = dance(moves, size, 10**9)
	enough = 10**9 % cycle
	return dance(moves, size, enough)


def spin(data, x):
	return data[-x:] + data[:-x]


def exchange(data, a, b):
	data = list(data)
	data[a], data[b] = data[b], data[a]
	return ''.join(data)


def partner(data, a, b):
	a, b = data.index(a), data.index(b)
	return exchange(data, a, b)


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	if mode == '1':
		func = dance
	if mode == '2':
		func = part2
	print(func(sys.stdin.read().strip()))


if __name__ == '__main__':
	main()
