#!/usr/bin/env python3
# encoding: utf-8

import ben

def sum_checksum(row):
	row = tuple(row)
	return max(row) - min(row)


def div_checksum(row):
	row = tuple(row)
	for i, el1 in enumerate(row):
		for el2 in row[i+1:]:
			els = el1, el2
			M, m = max(els), min(els)
			if M % m == 0:
				return M / m
	raise ValueError


def checksum(iterable, func):
	return sum(map(func, iterable))


def xinput():
	for line in ben.input_iter():
		yield map(int, line.split()


def main():
	import sys
	if sys.argv[1] == '1':
		func = sum_checksum
	elif sys.argv[1] == '2':
		func = div_checksum
	else:
		print('one or two only', file=sys.stderr)
		sys.exit(1)

	print(checksum(xinput(), func))

if __name__ == '__main__':
	main()
