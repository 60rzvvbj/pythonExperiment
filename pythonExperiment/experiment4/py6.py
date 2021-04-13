# 6．练习随机数应用。请生成50个随机数据，模拟一个班的考试成绩（要求在40～100分之间）。
# 计算这批数据的平均分、最高分和最低分，并排序由高到低输出。
import random
lst = [random.randint(40, 100) for i in range(0, 50)]
print('成绩为：')
print(lst)
print('最高分：{}，最低分{}，平均分{}'.format(max(lst), min(lst), sum(lst) / len(lst)))
lst.sort()
lst = lst[::-1]
print('排序后：')
print(lst)
