#!/usr/bin/env python3
# encoding: utf-8

import sys

from ben import input_iter


def answer(data, day2):
	data = data.split('\n')
	a = int(data[0].split()[-1])
	b = int(data[1].split()[-1])
	a_factor = 16807
	b_factor = 48271

	score = 0
	for i in range(40_000_000):
		print(i, file=sys.stderr, end='\b'*len(str(i)))
		a, b = next(a, a_factor), next(b, b_factor)
		if cmp(a, b):
			score += 1
	if day2:
		...
	return score


def cmp(a, b):
	def to_str(x):
		return bin(x)[2:]

	a, b = to_str(a), to_str(b)
	return a[-15:] == b[-15:]


def next(x, factor):
	return x * factor % (2**31-1)


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(sys.stdin.read(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
