# -*-coding:utf-8-*- #
import re
"""
# 从sql文件中获取某些issue_status的id
1. sql中内容保存成txt文件，然后从txt文件中获取，结果为一个字符串
2. 字符串拆分，一条数据一个字符串
"""

# 文件路径
txt_file_path = '/Users/zhanglinquan/Desktop/jiraissue.txt'

with open(txt_file_path, "r") as f:
    str_from_txt = f.read()



len_str_res = len(str_from_txt)

str_new = ''

# 循环判断字符串的值，如果等于左小括号，并且前一个值是英文逗号，在逗号后换行
for i in range(len_str_res):
    if i < len_str_res-1:
        if str_from_txt[i] == '(' or str_from_txt[i] == ')':
            if str_from_txt[i] == '(' and str_from_txt[i+1] == '1':
                str_new += '['
            if str_from_txt[i] == ')' and str_from_txt[i+1] == ',':
                str_new += ']'
                str_new += '\n'
        else:
            str_new += str_from_txt[i]
    else:
        str_new += ']'


# 拆分str
f = str_new.split('\n')

list_result = []

p1 = r"[0-9]\d*"
pattern1 = re.compile(p1)

for i in range(len(f)):
    list_result = f[i].split(',')
    if i == 0:
        issue_id = re.findall(pattern1, list_result[0])
        issue_status = re.findall(pattern1, list_result[13])
    else:
        issue_id = re.findall(pattern1, list_result[1])
        issue_status = re.findall(pattern1, list_result[14])
        if issue_status in (['10105'], ['10106'], ['10107'],['10108'],
                            ['10109'], ['10110'], ['10111'], ['10112'],
                            ['10114'], ['10115'], ['10116'], ['10117'],
                            ['10118'], ['10119'], ['10120'], ['10121'],
                            ['10122'], ['10123'], ['10124']):
            print(issue_id[0], issue_status[0])