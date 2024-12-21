import math
import itertools
import sys
from collections import defaultdict
sign=lambda x:(x>0)-(x<0)
nkpm={'0':(1,3),'1':(0,2),'2':(1,2),'3':(2,2),'4':(0,1),'5':(1,1),'6':(2,1),'7':(0,0),'8':(1,0),'9':(2,0),'A':(2,3)}
dkpm={'>':(2,1),'v':(1,1),'<':(0,1),'^':(1,0),'A':(2,0)}
inp=sys.stdin.read().strip()
mnp=defaultdict(list)
for i,(R,gy) in enumerate([(2,0),(4,3)]):
    for y1,x1,y2,x2 in itertools.product(range(R),range(3),range(R),range(3)):
        pathid=(i,y1,x1,y2,x2)
        dx,dy=sign(x2-x1),sign(y2-y1)
        ah,av=('<>'[dx==1])*abs(x2-x1),('^v'[dy==1])*abs(y2-y1)
        if (x2,y1)!=(0,gy):
            mnp[pathid].append('A'+ah+av+'A')
        if dx and dy and (x1,y2)!=(0,gy):
            mnp[pathid].append('A'+av+ah+'A')
dp=dict()
for (entry,R),dep in itertools.product(enumerate([2,4]),range(26)):
    for y1,x1,y2,x2 in itertools.product(range(R),range(3),range(R),range(3)):
        cmnp=mnp[(entry,y1,x1,y2,x2)]
        dp[(entry,dep,y1,x1,y2,x2)]=min([sum([dp[(0,dep-1,dkpm[x[i-1]][1],dkpm[x[i-1]][0],dkpm[x[i]][1],dkpm[x[i]][0])] for i in range(1,len(x))]) for x in cmnp]+[math.inf]) if dep or not len(cmnp) else len(cmnp[0])-1
ans=[0,0]
for x in inp.split('\n'):
    n,s=int(x[:3]),'A'+x
    for i,y in enumerate([2,25]):
        ans[i]+=sum([dp[(1,y,nkpm[s[j-1]][1],nkpm[s[j-1]][0],nkpm[s[j]][1],nkpm[s[j]][0])] for j in range(1,len(s))])*n
print(ans[0],ans[1])

