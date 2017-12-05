#!/usr/bin/env python3
# encoding: utf-8

import sys
from collections import Counter

from ben import input_iter

def valid(passphrase):
	counter = Counter()
	for word in passphrase.split():
		counter.update([word])
		if counter[word] > 1:
			return False
	return True


def has_anagram(passphrase):
	passphrases = Counter()
	for word in passphrase.split():
		word = tuple(sorted(word)) # don't ask
		passphrases.update([word])
		if passphrases[word] > 1:
			return True
	return False


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	valid_passphrases = (passphrase for passphrase in input_iter() if valid(passphrase))
	if mode == '1':
		print(len(valid_passphrases))
	elif mode == '2':
		print(len([p for p in valid_passphrases if not has_anagram(p)]))


if __name__ == '__main__':
	main()
