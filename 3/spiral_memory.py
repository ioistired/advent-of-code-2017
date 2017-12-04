#!/usr/bin/env python3
# encoding: utf-8

from collections import defaultdict, Iterable, namedtuple
from copy import copy
from math import ceil, floor, sqrt
import operator as operators
import sys


def get_coordinate(n):
		k=ceil((sqrt(n)-1)/2)
		t=2*k+1
		m=t**2
		t=t-1
		if n >= m - t:
			return k - (m-n), -k
		else:
			m -= t
		if n >= m - t:
			return -k, -k+(m-n)
		else:
			m -= t
		if n >= m-t:
			return -k+(m-n), k
		else:
			return k, k-(m-n-t)


def ismutable(x):
	try:
		hash(x)
	except:
		return True
	else:
		return False


def manhattan_distance(square):
	x2, y2 = get_coordinate(square)
	return abs(x2 - 0) + abs(y2 - 0)


def get_direction(n):
	"""which way to move to get to position n in the Ulam spiral"""
	return {
		1: Vector([1, 0]),
		2: Vector([0, 1]),
		3: Vector([-1, 0]),
		4: Vector([0, -1])
	}[floor(sqrt(4*n + 1) + 3) % 4 + 1]


def get_neighbors(coords):
	neighbors = []
	for Δx in range(-1, 2):
		for Δy in range(-1, 2):
			if (Δx, Δy) != (0, 0):
				neighbors.append(coords + Vector((Δx, Δy)))
	return neighbors


class Vector(tuple):
	def __new__(cls, *args):
		# if they try to construct it like old-style tuple
		# e.g. Vector([1, 2]), it should still work
		if len(args) == 1 and isinstance(args[0], Iterable):
			return cls.__new__(cls, *args[0])
		# allow construction via Vector(1, 2)
		# instead of tuple
		return super().__new__(cls, args)

	def __oper(self, other, operator):
		if isinstance(other, Iterable):
			new = list(other)
			for i, value in enumerate(self):
				try:
					new[i] = operator(new[i], value)
				except IndexError:
					raise ValueError('operands must have the same dimensions')
			return tuple(new)
		else:
			raise TypeError('operand must be iterable')

	def __add__(self, other):
		return self.__oper(other, operators.add)

	__radd__ = __add__

	def __sub__(self, other):
		return self.__oper(other, operators.sub)

	# subtraction is not commutative, so will this work?
	#__rsub__ = __sub__

	def __mul__(self, other):
		return self.__oper(other, operators.mul)

	#__rmul__ = __mul__

	def __truediv__(self, other):
		return self.__oper(other, operators.truediv)

	#__rtruediv__ = __truediv__


# part2
def stress_test(n):
	"""return the first value written that's larger than n"""
	current = (0, 0)
	vals = defaultdict(lambda: 0)
	vals[current] = 1 # given
	i = 0
	while vals[current] < n:
		current = get_direction(i) + current
		vals[current] = sum(map(vals.__getitem__, get_neighbors(current)))
		i += 1
	return vals[current]


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	puzzle_input = 289326
	if mode == '1':
		func = manhattan_distance
	elif mode == '2':
		func = stress_test

	print(func(puzzle_input))

if __name__ == '__main__':
	main()
