with open('input.txt') as f:
    input=f.read()

floor=0
char=0
for i in input:
    if floor==-1:
        break
    char+=1

    if i =='(':
        floor+=1
    else:
        floor-=1

o=open('output.txt','w')
print(char,file=o)
