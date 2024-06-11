
# REMove duplicates
num=[1,2,5,3,5]

dup=[]

for x in num:
    if x not in dup:
        dup.append(x)
print(dup)


