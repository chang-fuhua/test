import re

print('match code:' + str(re.match('cfh', 'cfh7061596')))

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
# (.*?) 表示"非贪婪"模式，只保存第一个匹配到的子串
matchObj = re.match('(.*) are (.*?) .*', line, re.M | re.I)
searchObj = re.search('(.*) are (.*?) .*', line, re.M | re.I)
if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")
if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.groups() : ", searchObj.groups())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("No match!!")