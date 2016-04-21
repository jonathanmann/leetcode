#most water

pts = [3,5,6,1,2,9,4,2,0,8,7,1]

def get_area(x1,y1,x2,y2):
    h = min(y1,y2)
    w = x2 - x1
    return h * w

def sol(pts):
    mx = 0
    for i,e in enumerate(pts):
        for j,m in enumerate(pts):
            tmp = get_area(i,e,j,m)
            if tmp > mx:
                mx = tmp
    return mx

def s(pts):
    mx = 0
    l = len(pts)

print sol(pts)
