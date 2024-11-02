'''i=eval(input('1.查询当前余额:'))
=eval(input('2.查询当前剩余流量'))
=eval(input('3.查询当前剩余通话余额'))'''
'''i = input()
while :
    i=input()
    if i=='1':
        print('当前余额为250')
    elif i=='2':
        print('流量250')
    elif i=='3':
        print('通话250')
    elif i=='0':
        break '''
#(1)初始化变量
answer='y'
#(2)条件判断
while answer=='y':
    #(3)循环操作
    print('--------欢迎使用10086查询功能')
    print('1.查询当前余额:')
    print('2.查询当前剩余流量')
    print('3.查询当前剩余通话余额')
    choice=input('请输入您要执行的操作：')#input的结果是字符串类型
    if choice=='1':
        print('当前余额为250')
    elif choice=='2':
        print('流量250')
    elif choice=='3':
        print('通话')
    elif choice=='0':
        print('exit')
        break
    else:
        print('XX')
    answer=input('操作有误，y/n')
else:
    print('exit')