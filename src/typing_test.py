import sys
import readchar

def typing_test(inp):
	sys.stdout.write(inp + "\b" * len(inp))
	sys.stdout.flush()
	b = list(inp)
	i = 0
	i2 = 0

	while True:
		k = readchar.readkey()
		while i2 == 0 and k in (readchar.key.BACKSPACE, "\x7f"):
			k = readchar.readkey()
		to_write = k
		if (i2 < len(inp) and k != inp[i2]) or i2 >= len(inp):
			if (k == ' '):
				to_write = f"\033[41m{k}\033[0m"
			else:
				to_write = f"\033[31m{k}\033[0m"
		i2 += 1
		if k in (readchar.key.ENTER, "\r", "\n"):
			break
		if k in (readchar.key.BACKSPACE, "\x7f") and i > 0:
			i -= 1
			i2 -= 2
			sys.stdout.write("\b")
			if (i2 < len(inp)):
				sys.stdout.write(inp[i2])
			else:
				sys.stdout.write(" ")
			sys.stdout.write("\b")
		elif len(k) == 1 and 32 <= ord(k) <= 126:
			if i < len(b):
				b[i] = k
			else:
				b.append(k)
			i += 1
			sys.stdout.write(to_write)
		sys.stdout.flush()

	print("\n")
	if "".join(b)[:i2 - 1] == inp:
		return True
	return False
