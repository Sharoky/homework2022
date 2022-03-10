with open('input.txt') as f:
    input=f.read()

floor=0
for i in input:
    if i =='(':
        floor+=1
    else:
        floor-=1

o=open('output.txt','w')
print(floor,file=o)
