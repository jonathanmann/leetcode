#Patch Array
import itertools

def pa(ar,n):
    nums = range(1,n + 1)
    p = 0
    for i in nums:
        if i not in ar:
            k = 2
            add_num = True
            while k <= len(ar) and add_num:
                for c in itertools.combinations(ar,k):
                    if sum(c) == i:
                        add_num = False
                        break
                k +=1
            if add_num:
                ar.append(i)
                p += 1
    return p

"""
ar = [1,3]
n = 6
ar = [1, 5, 10]
n = 20
"""
ar = [1,2,2]
n = 5
print pa(ar,n)

