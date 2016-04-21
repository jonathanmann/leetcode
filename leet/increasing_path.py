def get_moves(nums):
    r_len = len(nums)
    c_len = len(nums[0])
    rows = range(r_len)
    cols = range(c_len)
    paths = {}
    for r in rows:
        for c in cols:
            val = nums[r][c]
            paths[(r,c)] = [] 
            if r > 0:
                tv = nums[r-1][c]
                if tv > val:
                    paths[(r,c)].append((r-1,c))
            if r < r_len - 1:
                tv = nums[r+1][c]
                if tv > val:
                    paths[(r,c)].append((r+1,c))
            if c > 0:
                tv = nums[r][c-1]
                if tv > val:
                    paths[(r,c)].append((r,c-1))
            if c < c_len - 1:
                tv = nums[r][c+1]
                if tv > val:
                    paths[(r,c)].append((r,c+1))

    return paths

def walk(start,moves,scores):
    if start in scores:
        print "if",start,scores
        return scores[start]
    elif moves[start] == []:
        scores[start] = 0
        return 1
    else:
        w = 0
        t = 0
        for move in moves[start]:
            print 'move'
            try:
                t = walk(move,moves,scores) + 1
                print 't', t
            except:
                print "error"
            if t > w:
                w = t
                print 'assign',w,'to',start
                
        scores[start] = w 
        return scores[start]

        print "else",start,scores
                

def explore(moves):
    scores = {}
    frontier = moves.keys()
    explored = []
    while frontier:
        start = frontier.pop()
        if start in scores:
            pass   
        else:

            if moves[start] == []:
                scores[start] = 0
            else:
                walk(start,moves,scores)        

    return scores


nums = [[9,9,4],[6,6,8],[2,1,1]]
moves = get_moves(nums)

print explore(moves)
