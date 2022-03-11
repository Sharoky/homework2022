with open('input.txt') as f:
    input=f.readlines()

total=0

for i in input:
    l,w,h=i.split('x')
    bow=int(l)*int(w)*int(h)
    total+=bow

    max_side=max(int(l),int(w),int(h))
    ribbon=2*int(l)+2*int(w)+2*int(h)-2*max_side

    total+=ribbon

o=open('output.txt','w')
print(total,file=o)
