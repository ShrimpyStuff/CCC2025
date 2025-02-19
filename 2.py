pattern = input()
c = int(input())
cipher = ""
current = ""
groups = []
length = 0
for i in range(len(pattern)):
    current+=pattern[i]
    if (i+1)>=len(pattern):
        groups.append([current[0], int(current[1:])+length])
        length += int(current[1:])
        current = ""
    elif pattern[i+1].isalpha():
        groups.append([current[0], int(current[1:])+length])
        length += int(current[1:])
        current = ""

for pair in groups:
    # print(c%length)
    # print(pair)
    if (c%length)<pair[1]:
        print(pair[0])
        break
# print(c%length)