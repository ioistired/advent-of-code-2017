#!/usr/bin/env python3
# encoding: utf-8

import sys

import networkx as nx

def answer(input):
	graph = nx.DiGraph()

	for line in input.split('\n'):
		if not line:
			continue
		line = line.split()
		print(line)
		name = line[0]
		graph.add_node(name, weight=int(line[1].strip('()')))

		if '->' in line:
			children = (c.strip() for c in ''.join(line[3:]).split(','))

			for child in children:
				graph.add_edge(name, child)

	ordered = list(nx.topological_sort(graph))
	return ordered[0]


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	if mode == '1':
		print(answer(sys.stdin.read()))
	elif mode == '2':
		...


if __name__ == '__main__':
	main()
