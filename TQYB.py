# import requests
# import json
# for i in range(10,99):
#     try:
#         response = requests.get("http://www.weather.com.cn/adat/cityinfo/101{}0101.html".format(i))
#         res = response.content.decode('utf-8')
#         dict_res = json.loads(res)
#         city = dict_res['weatherinfo']['city']
#         w1 = dict_res['weatherinfo']['temp1']
#         w2 = dict_res['weatherinfo']['temp2']
#         print("城市{}".format(city))
#         print("最高温度{}，最低温度{}".format(w1,w2))
#         print("天气情况",dict_res['weatherinfo']['weather'])
#         print('*'*20)
#     except:
#         print("天气预报播报完毕")
#         break

'''
用类、对象、list实现以下场景：
1、添加学生
2、查看学生
3、退出
请选择:1
请输入学生姓名:zhangsan
请输入电话号:110
1、添加学生
2、查看学生
3、退出
请选择:2
姓名:zhangsan 电话号:110
1、添加学生
2、查看学生
3、退出
请选择:1
请输入学生姓名:lisi
请输入电话号:120
1、添加学生
2、查看学生
3、退出
请选择:2
姓名:zhangsan 电话号:110
姓名:lisi 电话号:120
1、添加学生
2、查看学生
3、退出
请选择:3
退出系统
'''