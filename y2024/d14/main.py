import math
import re
import sys
inp=sys.stdin.read().strip()
R,C=103,101
grid=[['.' for j in range(C)] for i in range(R)]
robots=[]
for x in inp.split('\n'):
    robots.append(list(map(int,re.findall(r'-?\d+',x))))
i=0
ans1,ans2=0,0
while not (ans1 and ans2):
    if i==100:
        quad=[0]*4
        for x in robots:
            quad[2*(x[0]<C//2)+(x[1]<R//2)]+=x[0]!=C//2 and x[1]!=R//2
        ans1=math.prod(quad)
    if not ans2:
        for x in robots:
            grid[x[1]][x[0]]='#'
        for x in robots:
            cntr=1
            while x[0]+cntr<C and grid[x[1]][x[0]+cntr]=='#':
                cntr+=1
            if cntr>8:
                ans2=i
                print('\n'.join([''.join(y) for y in grid]))
                break
    for j in range(len(robots)):
        grid[robots[j][1]][robots[j][0]]='.'
        for k in range(2):
            robots[j][k]=(robots[j][k]+robots[j][k+2])%([C,R][k])
    i+=1
print(ans1,ans2)

