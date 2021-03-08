intcode = [int(x) for x in input().split(',')]
print('input=', intcode)

for i in range(0, len(intcode), 4):
	opcode = intcode[i]
	if opcode == 1:
		intcode[intcode[i + 3]] = intcode[intcode[i + 1]] + intcode[intcode[i + 2]]
	elif opcode == 2:
		intcode[intcode[i + 3]] = intcode[intcode[i + 1]] * intcode[intcode[i + 2]]
	else:
		break
		
print('output=', intcode)