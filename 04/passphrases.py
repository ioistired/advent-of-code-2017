#!/usr/bin/env python3
# encoding: utf-8

import sys

from ben import input_iter

def has_duplicates(passphrase):
	seen_words = set()
	for word in passphrase.split():
		if word in seen_words:
			return True
		seen_words.add(word)

	return False


def has_anagram(passphrase):
	seen_words = set()
	for word in passphrase.split():
		word = tuple(sorted(word)) # don't ask
		if word in seen_words:
			return True
		seen_words.add(word)

	return False


def main():
	if len(sys.argv) == 1:
		print('Usage:', sys.argv[0], '<1|2> < input', file=sys.stderr)
		sys.exit(1)
	mode = sys.argv[1]
	valid_passphrases = (passphrase for passphrase in input_iter() if not has_duplicates(passphrase))
	if mode == '1':
		print(len(list(valid_passphrases)))
	elif mode == '2':
		print(sum(not has_anagram(p) for p in valid_passphrases))


if __name__ == '__main__':
	main()
