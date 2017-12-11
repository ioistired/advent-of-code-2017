#!/usr/bin/env python3
# encoding: utf-8

from collections import Counter
import sys

from ben import input_iter, Vector


def answer(data, day2):
	dmap = {
		"n": (0,1),
		"s": (0,-1),
		"ne": (.5,.5),
		"se": (.5,-.5),
		"nw": (-.5,.5),
		"sw": (-.5,-.5)
	}

	positions = set()
	current_pos = (0, 0)
	for direction in data.strip().split(','):
		current_pos += Vector(dmap[direction])
		positions.add(abs(current_pos[0])+abs(current_pos[1]))

	if day2:
		return max(positions)
	return abs(current_pos[0])+abs(current_pos[1])


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(sys.stdin.read(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
