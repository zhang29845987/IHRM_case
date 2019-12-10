# 导包
import unittest

import api
from api.api_employee import employee
from tools.assert_comm import asserts
from parameterized import parameterized

from tools.read_txt import read_text


# 创建员工增删改查类
class Test_employee(unittest.TestCase):

    def setUp(self) -> None:
        # 导入api层人员增删改查类
        self.emp = employee()

    # 添加员工
    #参数化添加员工数据
    @parameterized.expand(read_text)
    def test001(self, a, b, c):
        f = self.emp.post_employee(a, b, c)
        asserts(self, f, 200)
        api.user_id = f.json().get('data').get('id')
        print("添加员工：", f.text)
        asserts(self, f, 200)

    # 修改员工
    def test002(self):
        r = self.emp.put_employee("不会吐丝的蜘蛛侠")
        print("修改员工：", r.json())
        asserts(self, r, 200)

    # 查询员工
    def test003(self):
        r = self.emp.get_employee()
        asserts(self, r, 200)
        print("查询员工：", r.json())

    # 删除员工
    def test004(self):
        r = self.emp.delete_employee()
        print(r.text)
        print("删除员工:", r.json())
        asserts(self, r, 200)

    # 查询员工
    def test005(self):
        r = self.emp.get_employee()
        asserts(self, r, 200)
        print("查询员工:", r.json())
