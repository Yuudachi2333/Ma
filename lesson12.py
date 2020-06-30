# import os
# a = os.path.exists("D:\study\lesson\atest13\demo\aimg")
# if not a:
#     os.mkdir(r'D:\study\lesson\atest13\demo\aimg')
# import time
# file_name = time.strftime("%Y_%m_%d_%H%M%S")+".txt"
# print(file_name)
# file_path = 'D:\\study\\lesson\\atest13\demo\\aimg\\' + file_name
# print(file_path)
# f  = open(file_path,'w',encoding='utf-8')
# f.write("test")
# f.close()
import re

str1 = "hi1, i hiam tony,mike hi"
# re.findall()方法查找所以内容，返回所有匹配的结果，并存放在列表中
# print(re.findall("hi",str1))
# re.match()方法只有当被搜索字符串的开头匹配模式的时候，才能返回匹配的结果
# print(re.match('hi',str1))
# 如果match()有匹配，可以用group()显示出匹配的内容
# print(re.match('hi',str1).group())
# print(re.search('hi1',str1))
# print(re.search(string=str1,pattern='hi1'))
# print(re.search('hi',str1).group())
# print(re.findall('a.c',"axc"))
# print(re.findall('a\.c',"a.c"))
# print(re.findall('a[0-9]c',"a1c"))
# print(re.findall('a\dc',"aac"))
# print(re.findall('a[^\d]c',"acc"))
# print(re.findall('a\Dc',"acc"))
# print(re.findall('a\wc',"acc345c"))
# print(re.findall('a.*c',"acc"))
# print(re.findall('a\d*c',"a123dfc"))
# print(re.findall('a.+c',"ac"))
# print(re.findall('a.?c',"a1dc"))
# print(re.findall('a.{4}c',"a1ddec"))
# print(re.findall('a\d{4}c',"a12345c"))
# print(re.findall('a.{5,}c',"a234c"))
# print(re.findall('^ab',"abcfegh"))
# print(re.findall('eab$',"abcfeab"))
# print(re.findall('^f.*ah$',"fah"))

# 练习1：从字符串“site sea sue sweet see case sse ssee loses”中匹配出所有s开头，e结尾的单词
# str1='site sea sue sweet see case sse ssee loses'
# # print(re.findall('s\w+e',str1))
# print(re.findall(r'\bs[a-z]+e\b',str1))
# print(re.findall(r'\bs\S*?e\b',str1))
# print(re.findall(r'\bs\S*e\b',str1))
# print(re.findall('s\w*\Se\W',"site sea sue sweet see case sse ssee loses"))


# 练习2：匹配出一个字符串“My phonenumber is 12345678901” 中的手机号码

# str1= 'My phonenumber is 12345678901'
# print(re.findall('1\d{9}\d',"My phonenumber is 1234567890133"))
# print(re.findall('1[3-9]\d{8}\d',"My phonenumber is 13345678901"))
# print(re.findall('1\d{10}',"My phonenumber is 1"))
# print(re.findall('1\d{10}$',"My phonenumber is 1"))
# print(re.findall(r'\b[0-9]+',str1))
# d = re.findall(r'\d{11}',str1)
# print(d)

# p = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
# url = 'https://tool.oschina.net/uploads/apidocs/jquery/regexp.html'
# email = "wyu0430@163.com"
# print(re.findall(p,email))

# 非贪婪模式
# 总是尝试匹配尽可能多的字符；非贪婪的则相反，总是尝试匹配尽可能少的字符。
# print(re.match('ab*?','abbbb'))
# print(re.match('ab*','abbbb'))
# print(re.match('ab+','abbb'))
# print(re.match('ab+?','abbb'))
# print(re.match('ab??','abbb'))
# print(re.match('ab?','abbb'))
# print(re.match('ab{2,3}?','abbbb'))
# print(re.match('ab{2,3}','abbbb'))







