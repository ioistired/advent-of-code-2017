#!/usr/bin/env python3
# encoding: utf-8

import sys


def answer(instrs, day2=False):
	instrs = list(map(int, conv(instrs.split('\n'))))
	pos = 0
	i = 0
	while pos < len(instrs):
		old_pos = pos
		jmp = instrs[pos]
		pos += instrs[pos]
		if jmp >= 3 and day2:
			instrs[old_pos] -= 1
		else:
			instrs[old_pos] += 1

		i += 1

	return i


def conv(l):
	return (int(x) for x in l if x)


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)

	print(answer(sys.stdin.read(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
