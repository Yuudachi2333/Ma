import json

class OperationJson:
    # def __init__(self):
    #     self.data = self.read_data()

    def read_file_data(self):
        '''
        json 文件中读取数据成字典load
        :return:
        '''
        with open(r'D:\study\lesson\atest13\demo\api.json','r',encoding='utf-8') as fp:
            data = json.load(fp)
            return data

    def read_str_data(self):
        with open(r'D:\study\lesson\atest13\demo\api.json','r',encoding='utf-8') as fp:
            data = fp.read()
            res = json.loads(data)
            return res


    def get_keyTovaule(self,id):
        data = self.read_file_data()
        return  data[id]


    def write_json_file(self,dict1):
        '''
        dump 直接把字典写入json文件
        :param dict1:
        :return:
        '''
        with open(r'D:\study\lesson\atest13\demo\data.json','a',encoding="utf-8") as f:
            json.dump(dict1,f,ensure_ascii=False)

    def write_json_str(self,dict1):
        '''
        dumps把字典转换成str，再写入文件
        :param dict:
        :return:
        '''
        str1 = json.dumps(dict1)
        with open(r'D:\study\lesson\atest13\demo\data.json','a',encoding="utf-8") as f:
            f.write(str1+"\n")

if __name__ == '__main__':
    # json.dumps将Python对象编码成JSON字符串
    # json.loads将已编码的JSON字符串解码为Python对象
    f = OperationJson()
    # print(f.read_file_data())
    # print(f.read_str_data())
    # d = {"name":"tony","age":22}
    # d2 = {"name":"larry","age":33}
    # f.write_json_file(d)
    # f.write_json_str(d2)
    print(f.get_keyTovaule("error_code"))









