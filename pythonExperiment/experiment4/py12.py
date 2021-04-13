# 12. 编写函数getdigit(s)，提取出一个字符串中所有的数字，以列表形式返回。
# 例如有字符串“我的电话180, 学号 2,  班级号 1954201”, 则应返回['180', '2', '1954201'] 。
import re


def getdigit(s):
    return [x.lstrip("0") for x in re.findall("\d+", s)]


print(getdigit(input('请输入字符串：')))
