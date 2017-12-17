#!/usr/bin/env python3
# encoding: utf-8

import sys

from ben import CircularList


def answer(step_size, part2):
	step_size = int(step_size)
	buffer = [0]
	pos = 0
	for i in range(1, 2018):
		pos = (pos+step_size) % len(buffer) + 1
		buffer.insert(pos, i)

	if part2:
		...
	return buffer[buffer.index(2017)+1]


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(sys.stdin.read(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
