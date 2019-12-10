# 创建断言方法
def asserts(self, respoe, text):
    # 用过外部调用外部输入self方法，调用方法内部的断言方法
    # text预期结果，respoe实际结果
    self.assertEqual(text, respoe.status_code)
