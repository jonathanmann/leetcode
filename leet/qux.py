dep = {'foo' : ['baz','bar','eez'], 'bar' : ['baz'], 'baz' : ['qux'], 'qux' : [], 'eez' : [], 'nix':['baz']}

reqs = ['foo','nix']
reqs = ['nix']

def qux(reqs,dep):
    explored = []
    while reqs:
        r = reqs.pop()
        explored.append(r)
        for e in dep[r]:
            if e not in explored:
                reqs.append(e)
    return explored         


print qux(reqs,dep)    
            




