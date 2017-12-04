#!/usr/bin/env python3
# encoding: utf-8

from math import ceil, sqrt
import sys


def get_coordinate(n):
		k=ceil((sqrt(n)-1)/2)
		t=2*k+1
		m=t**2
		t=t-1
		if n >= m - t:
			return k - (m-n), -k
		else:
			m -= t
		if n >= m - t:
			return -k, -k+(m-n)
		else:
			m -= t
		if n >= m-t:
			return -k+(m-n), k
		else:
			return k, k-(m-n-t)


def manhattan_distance(square):
	x2, y2 = get_coordinate(square)
	return abs(x2 - 0) + abs(y2 - 0)


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	if mode == '1':
		square = 289326
	elif mode == '2':
		...
	print(manhattan_distance(square))


if __name__ == '__main__':
	main()