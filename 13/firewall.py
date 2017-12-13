#!/usr/bin/env python3
# encoding: utf-8

from collections import defaultdict
import sys

from ben import input_iter


class Scanner:
	def __init__(self, max_depth, position=0):
		self.max_depth = max_depth
		self.last_position = position
		self.position = position

	def move(self):
		last_position = self.last_position
		self.last_position = self.position

		if (
				self.position == 0
				or self.position > last_position
				and self.position < self.max_depth - 1):
			self.position += 1
		else:
			self.position -= 1

	def collides(self, spot=0):
		return self.position == spot

	def __repr__(self):
		return '{}({}, {})'.format(
			self.__class__.__name__,
			self.max_depth,
			self.position)


def get_depths(data):
	depths = {}
	for line in data:
		if not line:
			continue
		line = line.split(':')
		depths[int(line[0])] = int(line[1])
	return depths


def severity(data):
	depths = get_depths(data)
	severity = 0

	# depends on dicts being ordered
	scanners = {layer: Scanner(depth) for layer, depth in depths.items()}

	for packet_pos in range(max(depths)+1):
		#print(scanners)
		scanner = scanners.get(packet_pos)
		if scanner is None:
			advance(scanners)
			continue
		#print(packet_pos, scanner.max_depth, scanner.position)
		if scanner.collides():
			severity += depths.get(packet_pos, 0) * packet_pos

		advance(scanners)

	return severity


def min_delay(data):
	depths = get_depths(data)
	delay = 0
	safe = False
	while not safe:
		print(delay, end='\b'*len(str(delay)))
		safe = True
		for layer, depth in depths.items():
			if (layer+delay)%(2*depth-2) == 0:
				safe = False
				delay += 1
				break
	return delay


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)

	mode = sys.argv[1]
	if mode == '1':
		func = severity
	elif mode == '2':
		func = min_delay
	else:
		print('Modes 1 or 2 only', file=sys.stderr)
		sys.exit(1)

	print(func(sys.stdin.readlines()))


if __name__ == '__main__':
	main()
