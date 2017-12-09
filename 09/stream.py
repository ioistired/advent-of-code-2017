#!/usr/bin/env python3
# encoding: utf-8

import sys

def answer(stream, day2):
	score = 0
	should_ignore = False
	open_braces = 0
	open_angle = False
	garbage_count = 0
	for char in stream:
		if open_angle:
			if should_ignore:
				should_ignore = False
				continue
			elif char == '!':
				should_ignore = True
			elif char == '>':
				open_angle = False
			else:
				garbage_count += 1
		else:
			if char == '{':
				open_braces += 1
			elif char == '}':
				score += open_braces
				open_braces -= 1
			elif char == '<':
				open_angle = True

	return garbage_count if day2 else score


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(sys.stdin.read(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
