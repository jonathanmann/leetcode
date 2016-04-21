def cb(n,g):
    n = str(n)
    g = str(g)
    A = 0
    B = 0
    rg = ''
    rn = ''

    for i,c in enumerate(g):
        if n[i] == c:
            A += 1
        else:
            rg += c
            rn += n[i]
        
    for c in rg:
        if c in rn:
            B += 1            
            p = rn.find(c)
            if p != -1: 
                rn = rn[:p] + rn[p + 1:]

    return str(A) + "A" + str(B) + "B"

print cb(1252,2251)



