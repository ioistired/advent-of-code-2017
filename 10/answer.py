#!/usr/bin/env python3
# encoding: utf-8

from functools import reduce
import sys

def solve(ins, n=256, byte=False):
    skip_size = 0
    index = 0
    nums = list(range(n))
    if byte:
        ins = [ord(k) for k in ins] + [17, 31, 73, 47, 23]
    else:
        ins = [int(k) for k in ins.split(',')]
    n_iter = 1
    if bytes:
        n_iter = 64
    for _ in range(n_iter):
        s = ins[:]
        for length in s:
            seen = set()
            i = (index + length - 1) % n
            for j in range(index, index + length):
                j = j % n
                i = i % n
                if j in seen or i in seen:
                    break
                seen.add(j)
                seen.add(i)
                # print(i, j)
                nums[i], nums[j] = nums[j], nums[i]
                i -= 1
            index = (length + index + skip_size) % n
            skip_size += 1
    if not byte:
        return nums[0] * nums[1]
    dense = []
    for j in range(0, n, 16):
        val = reduce(lambda a, b: a ^ b, nums[j: j+16])
        hexed = hex(val).replace('0x', '')
        if len(hexed) == 1:
            hexed = '0' + hexed
        dense.append(hexed)
    return ''.join(dense)


def main():
	print(sys.argv[1] == '2')
	print(solve(sys.stdin.read().strip(), 256, sys.argv[1] == '2'))


if __name__ == '__main__':
	main()