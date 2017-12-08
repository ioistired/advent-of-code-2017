#!/usr/bin/env python3
# encoding: utf-8

import sys


def distribute(mem):
	left = max(mem)
	ptr = mem.index(left)
	mem[ptr] = 0

	while left:
		ptr += 1
		ptr %= len(mem)
		mem[ptr] += 1
		left -= 1

	return mem

# heavily inspired by
# https://www.reddit.com/r/adventofcode/comments/7hvtoq/2017_day_6_solutions/dqu82yf/
def answer(mem, day2):
	seen = set()
	reallocations = 0

	while tuple(mem) not in seen:
		seen.add(tuple(mem))
		distribute(mem)
		reallocations += 1

	# we're now in a state that we've seen
	# so solving the challenge again will tell us how many times it takes
	# to get back to this state
	if day2:
		return answer(mem, False)
	return reallocations


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(list(map(int, input().split())), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
