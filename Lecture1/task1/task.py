with open('input.txt') as f:
    input=f.readlines()
input=[x.rstrip() for x in input]
list1=[]

for i in input:
    if i not in list1:
        list1.append(i)
list1.sort()
list1.pop()

list2=input[-1]
list2=list2.replace(" ", "")

o=open('output.txt','w')

for k in list2:
    if k in list1:
        list2.index(k)
        print(list1.index(k),file=o)
    else:
        print('-1',file=o)
o.close()
