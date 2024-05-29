ND=input()
ND=ND.split(' ')
N=int(ND[0])
D=int(ND[1])
GlobalList=[]
CoordinatesList=[]
Count=1

while Count <= N:
    Count+=1
    Coordinates=input().split(' ')
    CoordinatesList.append(Coordinates)

YourLocation=input()
YourLocation=YourLocation.split(' ')
TargetLocation=input()
TargetLocation=TargetLocation.split(' ')

follow={}
def append_value(follow, x, y):
    if x in follow:
        if not isinstance(follow[x], list):
            follow[x] = [follow[x]]
        follow[x].append(y)
    else:
        follow[x] = [y]

for a in range(N):
    for b in range(N):
        Distance=(((int(CoordinatesList[a][0])-int(CoordinatesList[b][0]))**2)+((int(CoordinatesList[a][1])-int(CoordinatesList[b][1]))**2))**0.5
        if Distance <= D:
            append_value(follow, a, b)
            append_value(follow, b, a)

for c in range(N):
        Distance=(((int(CoordinatesList[c][0])-int(YourLocation[0]))**2)+((int(CoordinatesList[c][1])-int(YourLocation[1]))**2))**0.5
        if Distance <= D:
            append_value(follow, c, -1)
            append_value(follow, -1, c)

for d in range(N):
        Distance=(((int(CoordinatesList[d][0])-int(TargetLocation[0]))**2)+((int(CoordinatesList[d][1])-int(TargetLocation[1]))**2))**0.5
        if Distance <= D:
            append_value(follow, d, -2)
            append_value(follow, -2, d)

def ShortestPath():
    q = []
    visited = []
    q.append([-1])
    visited.append(-1)
    while q:
        path = q.pop(0)
        current = path[-1]
        if current == -2:
            for a in path:
                print ('y')
                return
        for l in follow.get(current, []):
          if l not in visited:
            newpath = list(path)
            newpath.append(l)
            visited.append(l)
            q.append(newpath)
    print ('n')

if ((int(YourLocation[0])-int(TargetLocation[0]))**2+(int(YourLocation[1])-int(TargetLocation[1]))**2)**0.5 <= D:
    print('y')
else:
    ShortestPath()
