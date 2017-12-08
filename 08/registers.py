#!/usr/bin/env python3
# encoding: utf-8

from collections import defaultdict
import operator
import sys

from ben import input_iter


operators = {
	'>': operator.gt,
	'>=': operator.ge,
	'<': operator.lt,
	'<=': operator.le,
	'==': operator.eq,
	'!=': operator.ne,
	'inc': operator.add,
	'dec': operator.sub,
}


def parse(instruction):
	instruction, _, condition = instruction.partition(' if ')
	instruction = instruction.split()
	register = instruction[0]
	operator = operators[instruction[1]]
	value = int(instruction[2])

	test_register, test_operator, test_value = condition.split()
	test_operator = operators[test_operator]
	test_value = int(test_value)

	return register, operator, value, test_register, test_operator, test_value


def execute(registers, instruction):
	register, operator, value, test_register, test_operator, test_value = parse(instruction)

	# dewit
	new_value = registers[register]
	if test_operator(registers[test_register], test_value):
		new_value = operator(registers[register], value)
		registers[register] = new_value
	return new_value


def answer(instructions, day2):
	registers = defaultdict(lambda: 0)
	seen_values = set()

	for instruction in instructions:
		new_value = execute(registers, instruction)
		seen_values.add(new_value)

	if day2:
		return max(seen_values)
	return max(registers.values())


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	print(answer(input_iter(), sys.argv[1] == '2'))


if __name__ == '__main__':
	main()
