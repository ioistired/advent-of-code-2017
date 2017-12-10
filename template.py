#!/usr/bin/env python3
# encoding: utf-8

import sys

from ben import input_iter


def answer(data, day2):
	...


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(sys.stdin.read(), sys.argv[1] == '2')
	print(answer(input_iter(), sys.argv[1] == '2')


if __name__ == '__main__':
	main()
