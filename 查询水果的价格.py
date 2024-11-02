s = 0
while s<5:
    print('[1]apple')
    print('[2]pear')
    print('[3]orange')
    print('[4grape]')
    print('[0]exit')
    i=input('请输入代表水果的数字：')
    if i=='1':
        print('prince=3.00')
        s+=1
    elif i=='2':
        print('prince=2.50')
        s+=1
    elif i=='3':
        print('4.10')
        print(s)
        s+=1
    elif i=='4':
        print('prince=10.20')
        s+=1
    elif i=='0':
        print('exit')
        break
else:
    print('exit')
