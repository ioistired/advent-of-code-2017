#!/usr/bin/env python3
# encoding: utf-8

import sys

from ben import input_iter


def do_until(x, func, condition):
	while True:
		x = func(x)
		if condition(x):
			break
	return x


def gen(start, factor, multiple=1):
	# an actual generator lol
	x = start
	func = lambda x: x*factor % (2**31-1)
	condition = lambda x: x % multiple == 0
	while True:
		x = do_until(x, func, condition)
		yield x


def answer(data, day2):
	data = data.split('\n')

	a = gen(int(data[0].split()[-1]), 16807, 4 if day2 else 1)
	b = gen(int(data[1].split()[-1]), 48271, 8 if day2 else 1)

	score = 0
	for i in range(5_000_000 if day2 else 40_000_000):
		print(i, file=sys.stderr, end='\b'*len(str(i)))
		if cmp(next(a), next(b)):
			score += 1
	# sometimes the status line isn't cleared fully
	# leading to wrong answers printed
	print()

	return score


def cmp(a, b):
	return a & 0xFFFF == b & 0xFFFF



def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(sys.stdin.read(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
