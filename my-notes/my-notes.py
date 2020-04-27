def sum_of_word(word):
    sum =0
    for char in word:
        sum+=ord(char) -96
    return sum
with open('rs.txt','w') as rs:
# 学习VS的内容的快捷键需要刻意练习
    