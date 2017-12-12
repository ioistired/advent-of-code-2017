#!/usr/bin/env python3
# encoding: utf-8

from collections import defaultdict
import sys

from ben import input_iter


def answer(data, day2):
	comms = defaultdict(lambda: [])
	for line in data:
		line = line.split('<->')
		prog = int(line[0])
		progs = map(int, line[1].split(','))
		comms[prog].extend(progs)

	comm_zero = [0]
	for prog in comms.keys():
		progs = comms[prog]
		if prog == 0 or 0 in progs:
			comm_zero.append(prog)
	if day2:
		...
	return len(comm_zero)


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(input_iter(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
