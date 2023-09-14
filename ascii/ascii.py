from functools import reduce


def to_ascii_code(inp):
	return [ord(c) for c in inp]


def from_ascii_code(inp):
	return reduce(lambda x, y: x + chr(y), inp, "")
