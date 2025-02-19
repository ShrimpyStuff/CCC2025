inputline = input()
inputs = inputline.split(" ")

lengths = [int(inputs[0]), int(inputs[2])]
widths = [int(inputs[1]), int(inputs[3])]

p1 = 2 * (sum(lengths) + max(widths))
p2 = 2 * (sum(widths) + max(lengths))

size = min(p1, p2)

print(size)