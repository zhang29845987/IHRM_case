import os


# 创建获取文件路径方法
def data_path():
    # 获取当前文件路径绝对路径
    path = os.path.dirname(os.path.abspath(__file__))
    # 把文件路径返回到函数中
    return path + "\data.json"
