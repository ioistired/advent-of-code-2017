#!/usr/bin/env python3
# encoding: utf-8

from math import ceil, sqrt
import itertools
import sys

i = 1j


#def get_coordinate(n):
#	# https://web.archive.org/web/20141202041502/http://danpearcymaths.wordpress.com/2012/09/30/infinity-programming-in-geogebra-and-failing-miserably/
#	p = _p(n)
#	# the formula he gave starts by going up, but we start by going right
#	# therefore, we need to multiply by -i to rotate -90°
#	z = (n-floor(p**2/4))*i**p + (floor((p+2)/4)-(floor((p+1)/4)*i))*i**(p-1)
#	return int(z.real), int(z.imag)


#def _p(n):
#	return floor((4*n+1)**0.5)

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