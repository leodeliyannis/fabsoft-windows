#!/usr/bin/env python

from sys import stdin

ls = []

for line in stdin:
	ls.append(line)

ls = sorted(ls, key = lambda s: s.lower())
for x in ls:
	print("cinst -y " + x, end="")
