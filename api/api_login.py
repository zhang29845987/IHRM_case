# 导包
import requests

import api


# 创建登陆类
class IHRM_login(object):
    # 初始化登陆类
    def __init__(self):
        # 导入登陆方法
        self.requsts = requests

    # 创建登陆方法
    def login(self, mobile, password):
        # 调用外部方法，产出数据存储成键和值
        self.data = {"mobile": mobile, "password": password}
        # 通过post请求登录，登陆成功把返回结果方法到函数中
        return self.requsts.post(url=api.url + "/api/sys/login", json=self.data, headers=api.Headers)
