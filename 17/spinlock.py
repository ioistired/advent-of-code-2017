#!/usr/bin/env python3
# encoding: utf-8

from collections import deque
import sys

from ben import CircularList


def part1(step_size):
	step_size = int(step_size)
	buffer = deque([0])
	pos = 0
	for i in range(1, 2018):
		pos = (pos+step_size) % len(buffer) + 1
		buffer.insert(pos, i)

	return buffer[buffer.index(2017)+1]


def part2(step_size):
	step_size = int(step_size)
	length = 1
	when = 0
	pos = 0
	for i in range(50_000_001):
		pos = (pos+step_size) % length + 1
		length += 1
		if pos == 1:
			when = i
	return when+1


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print((part2 if sys.argv[1] == '2' else part1)(sys.stdin.read()))


if __name__ == '__main__':
	main()
