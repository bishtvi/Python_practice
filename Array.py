#all the values should be on Same type

#need to import array

from array import *

val = array('i', [5,9,8,4,2])

print(val.buffer_info())
print(val[0])
for i in val:
     print(i)

##############

vals = array('i',[5,9,8,4,2])
newArr = array(vals.typecode,(a*a for a in vals))
for e in newArr:
      print(e)

########
vals = array('i', [5,9,8,4,2])

newArr = array(vals.typecode,(a*a for a in vals))

i = 0

while i< len(newArr):
    print(newArr[i])
    i=i+1
#######

#creating an empty array
arr = array('i', [])
n = int(input("Enter the value of the array "))

for i in range(n):
    x = int(input("Enter the next value : "))
    arr.append(x)

print(arr)
