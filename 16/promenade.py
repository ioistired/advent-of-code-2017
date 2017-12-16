#!/usr/bin/env python3
# encoding: utf-8

from string import ascii_lowercase
import sys

from ben import input_iter


def answer(moves, day2, size=16):
	moves = moves.split(',')
	progs = ascii_lowercase[:size]

	for move in moves:
		print(move)
		if move[0] == 's':
			progs = spin(progs, int(move[1:]))
		if move[0] == 'x':
			progs = exchange(progs, *map(int, move[1:].split('/')))
		if move[0] == 'p':
			progs = partner(progs, *move[1:].split('/'))

	if day2:
		...
	return progs


def spin(data, x):
	if x == 1:
		return data[-1] + data[:-1]
	return data[x-1:] + data[:x-1]


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
	print(answer(sys.stdin.read().strip(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
