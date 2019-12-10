# 导包
import unittest
from report import HTMLTestReportCN

# 导入测试用例
suite = unittest.defaultTestLoader.discover("./scripts")

if __name__ == '__main__':
    # 打开文件流




    with open("./report/report.html", "wb") as f:
        # 创建测试报告测试套件
        runner = HTMLTestReportCN.HTMLTestRunner(stream=f)
        # 运行测试用例
        runner.run(suite)
