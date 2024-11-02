num=eval(input('请输入四位数：'))
a=num//1000
b=num//100
c=num//10
e=b%10
f=c%10
g=num%10
print(a,e,f,g)
print('千位是：',a)
print('百位是：',e)
print('十位是：',f)
print('个位是：',g)

print('-*40')
num=eval(input('请输入四位数：'))
print('千位是：',num//1000)
print('百位是：',num//100%10)
print('十位是：',num//10%10)
print('个位是：',num%10)

print('-*40')
num=input('请输入一个四位数：')#num是一个字符串
print('千位上的数：',num[0])
print('百位上的数：',num[1])
print('十位上的数：',num[-2])
print('个位数上的数：',num[3])

