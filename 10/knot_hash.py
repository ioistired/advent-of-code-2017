#!/usr/bin/env python3
# encoding: utf-8

import sys

from captcha import CircularList

def answer(lens, day2, list_size=256):
	l = CircularList(x for x in range(list_size))
	lens = list(map(int, lens.split(',')))
	current_pos = 0
	skip_size = 0
	print(l)

	for length in lens:
		for i in range(current_pos, current_pos+length):
			l[i] = l[current_pos+length-i]
		#l[current_pos:current_pos+length] = reversed(l[current_pos:current_pos+length])
		current_pos += length + skip_size
		skip_size += 1
		print(l, file=sys.stderr)
	#print(l, file=sys.stderr)
	return l[0]*l[1]


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(sys.stdin.read(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
