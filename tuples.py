# tup=(1,"sumit",True)
# print(type(tup),tup)
# print(tup[0])
# print(tup[1])
# print(tup[2])
# if "sumit" in tup:
#     print("yes")
# else:
#     print("noi.")
# tup2=tup
# print(tup2[1:3])
#TUPLES ARE IMUTABLE SO IF WE WANT TO MAKE CHANGE IN THIS WE CONVERT IT INTO LIST THEN FOLLOW REVERSE PROCESS 
countries=("India", "span","Englend","singapore")
temp=list(countries)
temp.append("Russia")#add item
temp[2]="finland"#change item
temp.pop(3)#remove item
countries=tuple(temp)
print(type(countries))
desh=("palisthan", "china","austrelia")
c=countries+ desh 
print(c)


