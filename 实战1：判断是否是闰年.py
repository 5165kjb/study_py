year=eval(input('请输入年份：'))
if year%4==0 and year%100!=0 or year%400==0:
    year = eval(input('请输入年份：'))
    print('',year,'年是闰年')
else:
    print('不是闰年')