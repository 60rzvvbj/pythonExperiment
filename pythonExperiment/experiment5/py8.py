import jieba
import wordcloud

r = open('resources/smoker.txt', 'r', encoding='gbk')
s = r.read()
lst = list(jieba.cut(s, cut_all=False))
w = wordcloud.WordCloud(background_color='skyblue')
w.generate(' '.join(lst))
w.to_file('resources/smoker.png')
