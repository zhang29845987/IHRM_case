# 导包
import unittest

import api
from api.api_login import IHRM_login
from tools.assert_comm import asserts


# 创建接口测试登陆类
class Test(unittest.TestCase):
    # 创建类方法，在每条测试用例开始之前执行
    def setUp(self) -> None:
        self.login = IHRM_login()

    # 创建测试用例01
    def test001(self):
        # 调用api层登陆方法
        tt = self.login.login("13800000002", "123456")
        # 把相应数据以json格式显示出来
        data = tt.json()
        # 把相应结果data用户令牌取出存入变量
        token = data.get('data')
        # 重点：把data数据存入 api.Headers 请求头中 以下这种存入方式是在 api.Headers 字典变量中追加数据
        # 重点注意：Bearer 后面要加一个空格
        api.Headers["Authorization"] = "Bearer " + token
        # 导入断言
        asserts(self, tt, 200)
