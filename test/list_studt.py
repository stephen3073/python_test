# a=[i for i in range(3)]
# b=[j for j in range(4,8)]
# print(a)
# print(b)
# a.extend(b)
# print(a)
# c=zip(a,b)
# print(list(c))
aa=[
    [1,2,3],
    [4,5,6],
    [5,6,7]
]
print(aa)
bb=[[i[j] for i in aa ] for j in range(3)]
print(bb)

# for i in aa:
#     c=list(zip(i))
# print(c)
print(list(zip(aa[0],aa[1],aa[2])))
print(list(zip(*aa)))

b=[1,2,3]
print(list(zip(b)))

for i in range(1,11):
    # print("{0} {1} {2}".format(i,i*i,i*i,i))
    print("{0:2d} {1:3d} {2:4d}".format(i,i*i,i*i,i))