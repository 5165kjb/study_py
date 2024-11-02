#(初始化变量)
i=0
while i<3:#(2)条件判断,0,1,2执行
    #(3)语句块
    user_name=input('请输入您的用户名：')
    pwd=input('请输入您的密码：')
    #登录操作， if...else...
    if user_name=='fzh'and pwd=='6':
        print('系统正在登入，请稍后')
        print('.....')
        print('逗你玩')
     #需要改变循环变量，目的；退出循环
        i=8 #在第三行判断，False，退出循环
    else:
        if i<3:
            print('用户名或密码不正确！您还有',2-i,'次机会')
            i+=1  #相当于i=i+1 #改变变量
#单分支判断
if i==3:
    print('对不起，三次均错误')