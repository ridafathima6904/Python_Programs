#linera search
listtwo=[5,1,4,2,8]
find=2
found=False
for i in range(len(listtwo)):
    if listtwo[i]==find:
        break
if found:
    print ("Found")
else:
    print("Not Found")