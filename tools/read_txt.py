# 导包
import json

from data import data_path


# 创建读取文件数据方法
def read_text():
    # 打开文件流
    with open(data_path(), "r", encoding="utf-8") as f:
        # 创建一个列表
        arr = []
        # 读取json 文件中的数据
        sss = json.load(f)
        # 通过json文件中的键，取出值
        username = sss.get("username")
        mobile = sss.get("mobile")
        workNumber = sss.get("workNumber")
        # 把取出json文件中的数据存入列表中
        arr.append((username, mobile, workNumber))
        print(arr)
    # 把列表值返回到函数中
    return arr
