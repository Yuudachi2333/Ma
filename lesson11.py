import requests
from urllib import request
import json
# url = "https://www.runoob.com/python3/python3-tutorial.html"
# respones = requests.get(url)
# print(respones.status_code)
dict1 = {
                        "id": 309,
                        "name": "小白",
                        "sex": "男",
                        "age": 28,
                        "addr": "河南省济源市北海大道32号",
                        "grade": "天蝎座",
                        "phone": "18512572946",
                        "gold": 100
                }
# loads传的是字符串,转换成字典
# with open(r"D:\study\lesson\atest13\demo\api.json",'r',encoding="utf-8") as f:
#     data = f.read()
# res = json.loads(data)
# for key,value in res.items():
#     print(key,value)
# print(res['stu_info'][0]['name'])

# load 传的是文件，把json文件内容转换成字符串
# with open(r"D:\study\lesson\atest13\demo\api.json",'r',encoding="utf-8") as f:
#     res = json.load(f)
# print(res)
# for key,value in res.items():
#     print(key,value)

# dumps传的是字典，把字典转换成json格式写入json文件
# res = json.dumps(dict1,ensure_ascii=False)
# with open(r'D:\study\lesson\atest13\demo\data.json','w',encoding='utf-8') as f:
#     f.write(res)
#
# dump传的是文件，把字典内容写入到文件为json格式
# with open(r'D:\study\lesson\atest13\demo\data.json','w',encoding='utf-8') as f:
#     json.dump(dict1,f,ensure_ascii=False)


