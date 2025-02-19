nmq = [int(num) for num in input().split()]
col = []
pret = []
cis = []
for i in range(nmq[0]):
    nums = [int(num) for num in input().split()]
    col.append(nums[0])
    pret.append(nums[1])
for i in range(nmq[2]):
    cis.append([int(num) for num in input().split()])

for q in range(nmq[2] + 1):

    best = list(range(nmq[1]+1))

    def pretty(i):
        return pret[i]

    for i in range(nmq[1]+1, len(col)):
        best.append(i)
        best.sort(key=pretty)
        best = best[1:]


    print(sum([pret[num] for num in best]))