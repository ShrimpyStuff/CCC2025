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

    best = [None] * nmq[1]

    def pretty(i):
        if i == None:
            return -1
        return pret[i]
    
    def duplicateColours(listB, addition):
        dupes = {}
        for i in listB+[addition]:
            if i == None: continue
            cCol = col[i]
            if cCol in dupes.keys():
                dupes[cCol].append(i)
            else: 
                dupes[cCol] = [i]
        return dupes

    for i in range(len(col)):
        dupes = duplicateColours(best, i)[col[i]]
        if len(dupes) > 2:
            for index in dupes:
                if pret[i] > pret[index]:
                    best.remove(index)
                    best.append(i)
                    best.sort(key=pretty)
                    break
        else:
            best.append(i)
            best.sort(key=pretty)
            best = best[1:]


    print(sum([pret[num] for num in best]))
    if q+1 > 0 and q+1 < nmq[2]+1:
        if cis[q][0] == 1:
            col[cis[q][1]-1] = cis[q][2]
        else:
            pret[cis[q][1]-1] = cis[q][2]
