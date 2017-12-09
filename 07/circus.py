#!/usr/bin/env python3
# encoding: utf-8

import collections
import sys

import networkx as nx
from ben import input_iter


# https://www.reddit.com/r/adventofcode/comments/7i44pg/2017_day_7_solutions/dqw0f0c/
def answer(input, part2):
	graph = nx.DiGraph()

	for line in input:
		if not line:
			continue
		line = line.split()
		name = line[0]
		graph.add_node(name, weight=int(line[1].strip('()')))

		if '->' in line:
			children = (c.strip() for c in ''.join(line[3:]).split(','))

			for child in children:
				graph.add_edge(name, child)

	ordered = list(nx.topological_sort(graph))
	if not part2:
		return ordered[0]

	weights = {}
	# Going backwards (starting from the leaves)
	for node in reversed(ordered):
		# Start with this nodes own weight
		total = graph.nodes[node]['weight']

		counts = collections.Counter(weights[child] for child in graph[node])
		unbalanced = None

		for child in graph[node]:
			# If this child's weight is different than others, we've found it
			if len(counts) > 1 and counts[weights[child]] == 1:
				unbalanced = child
				break

			# Otherwise add to the total weight
			val = weights[child]
			total += weights[child]

		if unbalanced:
			# Find the weight adjustment and the new weight of this node
			diff = weights[unbalanced] - val
			return graph.nodes[unbalanced]['weight'] - diff

		# Store the total weight of the node
		weights[node] = total



def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(input_iter(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
