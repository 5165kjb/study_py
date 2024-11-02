import random
rand=random.randint(1,100)
j=0
while j<100:
    i = eval(input('在我心里有个数，1-100间，请你猜一猜：'))
    if i>rand:
        print('big')
        j+=1
    elif i<rand:
        print('small')
        j+=1
    elif i==rand:
        print('yes')
        break
    elif i==0:
        print('rand')
print(j)