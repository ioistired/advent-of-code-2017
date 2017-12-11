#!/usr/bin/env python3
# encoding: utf-8

class CircularList(list):
	def __getitem__(self, x):
		if isinstance(x, slice):
			return CircularList(self[x] for x in self._rangeify(x))
		return super().__getitem__(self._wrap(x))

	def __setitem__(self, key, value):
		if isinstance(key, slice):
			...
		else:
			super().__setitem__(self._wrap(key), value)

	def _wrap(self, x):
		return x % len(self)

	def _rangeify(self, slice):
		start, stop, step = slice.start, slice.stop, slice.step
		if start is None:
			start = 0
		if stop is None:
			stop = len(self)
		if step is None:
			step = 1
		if step < 0:
			start, stop = stop-1, start-1
		# stop at the end, because the new slice shouldn't repeat
		return range(start, max(len(self), stop), step)

def captcha(x, step):
	t = CircularList(map(int, x))

	sum = 0
	for i, digit in enumerate(t):
		if digit == t[i+step]:
			sum += t[i]

	return sum


def main():
	import sys
	if sys.argv[1] == '1':
		print(captcha(input(), 1))
	elif sys.argv[1] == '2':
		x = input()
		print(captcha(x, len(x)//2))
	else:
		print(
			'Need one or two depending on which part to solve.',
			file=sys.stderr
		)


if __name__ == '__main__':
	main()
