##########################################################
import sys
input = sys.stdin.readline
def ii():return int(input())
def mii():return map(int,input().rstrip().split())
def lmii():return list(map(int,input().rstrip().split()))
##########################################################

n = ii()
tree = dict()
for _ in range(n):
    a,b = mii()
    if a in tree:
        if tree[a]>b:
            tree[a] = b
    else:
        tree[a] = b
# st = sorted(tree.items())
# print(st)
st = sorted(tree.items(),key=lambda x: x[1])
print(st)
prev= st[0][1]
ans = 1
for a,b in st:
    if a>=prev:
        ans+=1
        prev=b
print(ans)
    


    
    