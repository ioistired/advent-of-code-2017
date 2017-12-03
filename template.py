#!/usr/bin/env python3
# encoding: utf-8

import sys

def answer():
	...


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	if mode == '1':
		...
	elif mode == '2':
		...
	print(answer(,))


if __name__ == '__main__':
	main()
