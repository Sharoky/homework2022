with open('input.txt') as f:
    input=f.readlines()

total=0

for i in input:
    l,w,h=i.split('x')
    s=2 * int(l) * int(w) + 2 * int(w) * int(h) + 2 * int(h) * int(l)
    total+=s

    min_side=min(int(l)*int(w),int(l)*int(h),int(w)*int(h))
    total+=min_side

o=open('output.txt','w')
print(total,file=o)
