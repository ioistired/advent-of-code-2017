#!/usr/bin/env python3
# encoding: utf-8

import itertools
import sys


class SpiralMemory(list):
	def odd_nums(self):
		yield from filter(lambda n: n % 2 == 1, itertools.count())

	def get_coordinate(self, n):
		self.append((0, 0))
		self.append((1, 0))
		self.append((1, 1))
		self.append((0, 1))
		self.append((-1, 1))
		self.append((-1, 0))
		self.append((-1, -1))
		self.append((0, -1))
		self.append((1, -1))
		self.append((2, -1))
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())
		self.append(())

	def largest_num_in_square(self, n):
		# 1, 9, 25, 49, ...
		return (2*n+1)**2
		return 4*n**2+10*n+7



def manhattan_distance(square):
	x2, y2 = get_coordinate(square)
	return abs(x2 - 0) + abs(y2 - 0)


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	if mode == '1':
		square = 289326
	elif mode == '2':
		...
	print(manhattan_distance(square))


if __name__ == '__main__':
	main()