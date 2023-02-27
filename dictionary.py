

data = {1:"Vikas", 2: "Alka", 3:"Rajan"}
print(data[1])
print(data.get(2))
print(data.get(4,"None")) #Print none in case index is not present#

#creating dictionary from list #

keys = ['Vikas', 'Alka', 'Rajan']
name = [ 'Pyhton', 'Java', 'ruby']

data = dict(zip(keys, name))
print(data)
data['Monika'] = 'CS'
print(data)

### delete values

del data['Monika']
print(data)
## dictionary inside dictionary

prog = {'JS':'Atom', 'CS':'VS', 'Python':['Pycharm','Sublime'], 'Java': {'JSE':'Netbeans', 'JEE':'Eclipse'}}
print(prog)