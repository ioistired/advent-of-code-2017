#!/usr/bin/env python3
# encoding: utf-8

import pprint
import sys

from ben import flatten
import knot_hash


pp = pprint.PrettyPrinter()


def hash(data):
	return hex2bin(knot_hash.solve(data, 256, True))


def hex2bin(data):
	h2b = {
    	'0': '0000',
    	'1': '0001',
    	'2': '0010',
    	'3': '0011',
    	'4': '0100',
    	'5': '0101',
    	'6': '0110',
    	'7': '0111',
    	'8': '1000',
    	'9': '1001',
    	'a': '1010',
    	'b': '1011',
    	'c': '1100',
    	'd': '1101',
    	'e': '1110',
    	'f': '1111'
	}
	return ''.join(h2b[c] for c in data)


def answer(data, day2):
	rows = []
	for i in range(128):
		row = []
		for c in hash('{}-{}'.format(data, i)):
			row.append(c == '1')
		rows.append(row)

	for row in rows[:8]:
		print(''.join('#' if c else '.' for c in row[:8]))

	if day2:
		...
	return sum(flatten(rows))



def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(sys.stdin.read().strip(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
