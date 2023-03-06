av = 7
x = int(input("How many candies you want? "))

i = 1
while i<=x:
    if i > av:
        break
    print("candy")
    i+=1
print("bye")

################
for i in range(1,101):
    if i%3==0 or i%5==0:
        continue
    print(i)

###############

for i in range(1, 101):

    if i%2!=0:
        pass
    else:
        print(i)