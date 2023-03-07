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
