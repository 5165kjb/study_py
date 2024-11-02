row=eval(input('请输入行数：'))
while row%2==0:   #判断行数的奇偶数，菱形中间一行最长，
    print('重新输入菱形的行数：')
    row=eval(input('请输入行数4'))
#输出菱形
'''
&&&*
&&***
&*****
*******
&*****
&&***
&&&*
7行
'''
top_row=(row+1)//2
#上半部分
for i in range(1,top_row+1):
    #倒三角
    for j in range(1,top_row+1-i):
        #print('&',end='')
        print(' ',end='')#空格才能占位置
    #等腰三角形
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print() #当两个并列的for内循环结束，换行
#下半部分
bottom_row=(row+1)//2
for i in range(1,bottom_row):
    #直角三角形
    for j in range(1,i+1):
        print(' ',end='')
    #等腰三角形
    for k in range(1,(bottom_row-i)*2):
        if k==1 or k==(bottom_row-i)*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()