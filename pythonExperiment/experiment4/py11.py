# 11. 编写一个函数isGoodpwd(s)，检查传入的字符串s是否是一个好密码，返回True或False。
# 好密码的标准：密码长度>=8, 只能由字母和数字构成
# 且必须同时含有大小写字母和数字，不能含有空格和标点符号等特殊字符。
def isGoodpwd(s):
    return len(s) >= 8 and s.isalnum() and not s.isalpha() and not s.isdigit() and not s.islower() and not s.isupper()

print(isGoodpwd('dadsd123AS'))
print(isGoodpwd('dadsdASASD'))
print(isGoodpwd('dadsd 123AS'))
print(isGoodpwd('d12AS'))
print(isGoodpwd('131231212AS'))
