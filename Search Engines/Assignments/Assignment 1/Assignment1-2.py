#!/usr/bin/python
# Guido Cnossen


def bigram(l1,l2):
	it1 = iter(l1)
	it2 = iter(l2)
	sol = []

	n1 = next(it1)
	n2 = next(it2)
	while True:
		try:
			if n1 == (n2-1):
				return True
			else:
				if n1 < (n2-1):
					n1 = next(it1)
				else:
					n2 = next(it2)
		except StopIteration:
			return False
